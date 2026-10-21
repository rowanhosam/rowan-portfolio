"""Run with: ANTHROPIC_API_KEY=test pytest (from the api/ folder). Claude is faked; no API calls."""
import importlib
from types import SimpleNamespace

import pytest
from fastapi.testclient import TestClient

import main


def fake_reply(text, stop_reason="end_turn"):
    async def create(**kwargs):
        create.kwargs = kwargs
        return SimpleNamespace(stop_reason=stop_reason, content=[SimpleNamespace(type="text", text=text)])
    return create


@pytest.fixture
def api(monkeypatch):
    main.limiter.reset()
    return TestClient(main.app)


def test_answers_question_with_profile_in_system_prompt(api, monkeypatch):
    create = fake_reply("I build backends with FastAPI and PostgreSQL.")
    monkeypatch.setattr(main.client.messages, "create", create)
    r = api.post("/ask", json={"question": "What do you build?"})
    assert r.status_code == 200
    assert r.json() == {"answer": "I build backends with FastAPI and PostgreSQL."}
    assert create.kwargs["model"] == "claude-haiku-5-5"
    assert "Rowan Elansary" in create.kwargs["system"]
    assert create.kwargs["messages"][-1] == {"role": "user", "content": "What do you build?"}


def test_history_must_start_with_user_turn(api, monkeypatch):
    create = fake_reply("ok")
    monkeypatch.setattr(main.client.messages, "create", create)
    history = [{"role": "assistant", "content": "hi"}, {"role": "user", "content": "q1"}, {"role": "assistant", "content": "a1"}]
    api.post("/ask", json={"question": "q2", "history": history})
    assert [m["role"] for m in create.kwargs["messages"]] == ["user", "assistant", "user"]


def test_refusal_returns_fallback(api, monkeypatch):
    monkeypatch.setattr(main.client.messages, "create", fake_reply("", stop_reason="refusal"))
    assert api.post("/ask", json={"question": "x"}).json()["answer"] == main.FALLBACK


@pytest.mark.parametrize("body", [{"question": ""}, {"question": "x" * 301}, {"question": "q", "history": [{"role": "system", "content": "x"}]}])
def test_rejects_bad_input(api, body):
    assert api.post("/ask", json=body).status_code == 422


def test_rate_limited_per_visitor(api, monkeypatch):
    monkeypatch.setattr(main.client.messages, "create", fake_reply("ok"))
    codes = [api.post("/ask", json={"question": "hi"}).status_code for _ in range(7)]
    assert codes[:6] == [200] * 6 and codes[6] == 429


def test_site_wide_daily_cap(monkeypatch):
    # With the site-wide cap set below the per-visitor limit, the cap is what stops the third question.
    monkeypatch.setenv("DAILY_CAP", "2")
    capped = importlib.reload(main)
    try:
        capped.limiter.reset()
        monkeypatch.setattr(capped.client.messages, "create", fake_reply("ok"))
        api = TestClient(capped.app)
        codes = [api.post("/ask", json={"question": "hi"}).status_code for _ in range(3)]
        assert codes == [200, 200, 429]
    finally:
        monkeypatch.delenv("DAILY_CAP")
        importlib.reload(main)


class FakeHttp:
    sent = []
    def __init__(self, *a, **k): pass
    async def __aenter__(self): return self
    async def __aexit__(self, *a): return False
    async def post(self, url, headers, json):
        FakeHttp.sent.append(json)
        return SimpleNamespace(status_code=200, text="ok")


def test_visit_emails_name_when_configured(api, monkeypatch):
    FakeHttp.sent = []
    monkeypatch.setenv("RESEND_API_KEY", "re_test")
    monkeypatch.setenv("ALERT_EMAIL", "me@example.com")
    monkeypatch.setattr(main.httpx, "AsyncClient", FakeHttp)
    r = api.post("/visit", json={"role": "recruiter", "track": "frontend", "name": "Sam"})
    assert r.status_code == 204
    assert FakeHttp.sent[0]["to"] == ["me@example.com"]
    assert FakeHttp.sent[0]["subject"] == "Sam (Recruiter · Front end) opened your portfolio"


def test_visit_is_quiet_without_keys(api, monkeypatch):
    FakeHttp.sent = []
    monkeypatch.delenv("RESEND_API_KEY", raising=False)
    monkeypatch.setattr(main.httpx, "AsyncClient", FakeHttp)
    assert api.post("/visit", json={"role": "curious", "name": "Ana"}).status_code == 204
    assert FakeHttp.sent == []


def test_visit_rejects_bad_input_and_floods(api, monkeypatch):
    monkeypatch.delenv("RESEND_API_KEY", raising=False)
    assert api.post("/visit", json={"role": "admin", "name": "x"}).status_code == 422
    assert api.post("/visit", json={"role": "curious", "name": ""}).status_code == 422
    codes = [api.post("/visit", json={"role": "curious", "name": "a"}).status_code for _ in range(4)]
    assert codes == [204, 204, 204, 429]

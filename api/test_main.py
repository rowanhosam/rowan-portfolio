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

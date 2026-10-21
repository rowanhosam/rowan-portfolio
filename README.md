# Rowan's Access Pass

A one-page portfolio built around an access-pass idea:

- **Talking intro tile**: plays `intro.mp4` with synced captions. Without a video it shows an animated stand-in avatar.
- **ID card**: CR80-proportioned card that tilts with the pointer and flips to show skills.
- **Passport stamps**: achievements as clickable stamps.
- **Terminal**: type `help` to explore skills, stack and projects.

## Make it yours

| What | Where |
| --- | --- |
| Intro video | transparent `media/intro.webm` (Chrome) + `media/intro-hevc.mp4` (Safari) |
| Captions | `CAPTIONS` array in the script (times in seconds) |
| Photo on the card | `media/photo.png` |
| Achievements | `STAMPS` array |
| Terminal answers | `CMDS` object |
| Email | `#email` in the footer and `hire` in the terminal |

No build step. Open `index.html` in a browser, or serve with `python3 -m http.server`.

## AI chat ("Ask me anything")

Visitors' questions go to a small FastAPI service in `api/`, which asks Claude Haiku and
answers in the speech bubble (and in the terminal for anything that isn't a command).
It only knows what's in `api/profile.md`; lines starting with `TODO` are ignored.

- Limits: 6 questions per visitor per day, and 300 a day site-wide (`DAILY_CAP`), via slowapi. At Claude Haiku 5.5 prices that caps spend at roughly $0.10 a day.
- Tests: `cd api && ANTHROPIC_API_KEY=test pytest` (Claude is faked, no cost).
- Run locally: `cd api && uvicorn main:app --reload --port 8000`, then serve the site with
  `python3 -m http.server 8080` and open http://localhost:8080.

### Deploy the API (Render, free)
1. New → Blueprint → pick this repo (it reads `render.yaml`).
2. Set `ANTHROPIC_API_KEY` in the Render dashboard.
3. If your site isn't at `https://rowanhosam.github.io`, change `ALLOWED_ORIGINS`.
4. If Render gives a different URL than `rowan-portfolio-api.onrender.com`, update `CHAT_API` in `index.html`.

## Access gate

First-time visitors pick **Recruiter**, **Engineer** or **Just curious**; the page then
reorders its sections and swaps the intro button, ask-box hint and brief for that role
(`ROLES` in the page script). The "Visitor · change" chip reopens it.

Share a link ending in `#recruiter`, `#engineer` or `#curious` to skip the gate with that role.

Recruiters also pick what they're hiring for (full stack, front end, back end, app/UX design,
AI/ML). That reorders the stamps, swaps the card-back skills, the "What I do" line, the ask-box
hint and the rotating headline word (`TRACKS` in the page script). Track links:
`#recruiter-fullstack`, `#recruiter-frontend`, `#recruiter-backend`, `#recruiter-design`, `#recruiter-ai`.

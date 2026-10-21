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
| Achievements | `STAMPS` array (remove `example: true` once real) |
| Terminal answers | `CMDS` object |
| Email | search for `hello@yourdomain.com` |

No build step. Open `index.html` in a browser, or serve with `python3 -m http.server`.

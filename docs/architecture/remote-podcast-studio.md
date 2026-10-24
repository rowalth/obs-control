# Remote Podcast Studio Architecture

## Outcome

A guest joins one familiar service while the host operates a consistent OBS production system.
The platform choice changes the capture path, not the scene names, audio roles, handoff, or safety rules.

## Mode boundary

Only one guest platform is active for a session:

- **Riverside:** default for nontechnical guests; downloaded isolated tracks are the master.
- **Microsoft Teams:** corporate fallback; OBS captures the program and separate host/call audio.
- **VDO.Ninja:** laboratory mode; isolated Solo links feed OBS Browser Sources after qualification.

The guest never joins multiple guest platforms for one session.

### Deferred platform: Jitsi Meet

Jitsi Meet is a future recording option, not an implemented v0.1 mode. A later phase
must qualify its corporate-browser compatibility, nontechnical guest journey, OBS
capture path, audio separation, recording ownership, and recovery behavior before a
runbook or production recommendation is added.

## Production layers

1. The invitation exposes one guest link and one human fallback contact.
2. The selected platform handles the conversation.
3. OBS composes reusable component scenes into program layouts.
4. OBS records a recoverable program file and audio tracks by role.
5. The session manifest identifies the primary masters, safety recording, ownership, and known compromises.

## Visual contract

The canonical scene and source roles live in `config/remote-podcast-scenes.json`.
Browser overlays render at 1920x1080 and keep text inside a five-percent title-safe margin.

The shared repository provides neutral placeholders.
The owning show repository supplies logo, colors, fonts, intro/outro media, and episode copy through `docs/templates/show-brand-handoff.md`.

## Audio contract

| Track | Role |
|---|---|
| 1 | Complete mix |
| 2 | Host microphone |
| 3 | Remote guest or call |
| 4 | Media and music |
| 5 | Additional guest or spare |

OBS uses 48 kHz audio.
The host microphone must not also arrive through captured application audio.

## Recording ownership

- Riverside isolated files remain authoritative in Riverside mode.
- OBS remains an independent safety/program reference in every mode.
- A Teams cloud recording is an optional backup whose owner and access policy must be recorded.
- VDO.Ninja browser recording is optional and never the only master.

## Repository boundary

This repository contains reusable definitions, overlays, scripts, and runbooks.
It does not contain live service URLs, credentials, guest data, show branding, or recordings.

Runtime files use `<show>/<YYYY-MM-DD>-<episode-slug>/` outside Git and receive a second copy before cleanup.

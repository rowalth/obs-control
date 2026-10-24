# Remote Podcast Preflight

Run this checklist 30 minutes before the guest arrives.
It is deliberately separate from the guest's 10-15 minute greenroom window.

## Repository and storage

1. Run `scripts/remote-podcast-validate`.
2. Set `REMOTE_PODCAST_RECORDING_DIR` to the episode's existing folder outside Git.
3. Run `scripts/remote-podcast-preflight --offline`.
4. Confirm the folder has enough free space and a second-copy destination is available.

## OBS inspection

1. Confirm OBS is not streaming, recording, or running the virtual camera.
2. Select the dedicated disposable or approved podcast profile and scene collection.
3. Confirm 1920x1080 at 30 fps and 48 kHz audio.
4. Confirm the scene names against `config/remote-podcast-scenes.json`.
5. Confirm track 1 is the full mix and tracks 2-5 follow `config/remote-podcast.defaults.json`.
6. Confirm the host microphone is not duplicated through captured application audio.
7. Confirm the lower-third and episode-title overlays stay inside the title-safe area.

Use the installed `obs-control` skill for live inspection.
Do not start a sample recording, virtual camera, stream, or destructive scene change without explicit approval.

## Platform

1. Open only the selected session mode: Riverside, Teams, or an approved VDO.Ninja laboratory session.
2. Verify the camera, microphone, speaker, and network path.
3. Confirm who owns the primary and backup recordings.
4. Confirm recording consent will be stated before capture begins.
5. Keep the Teams fallback ready when Riverside is the primary corporate-guest path.

## Guest greenroom

1. Admit the guest and confirm framing, eye line, light, and microphone selection.
2. Ask the guest to use headphones when available.
3. Confirm the guest can hear and be heard.
4. Explain that the guest should keep the browser or app open after recording until any upload completes.
5. Make a short sample only after the operator has approval to start recording.

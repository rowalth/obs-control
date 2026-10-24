# Microsoft Teams Runbook

Use Teams when a corporate guest cannot or will not use Riverside.
The baseline path uses ordinary window or application capture with application audio; NDI is not required.

## Meeting ownership

1. Prefer a meeting organized by the host so lobby, recording, and access policies are known.
2. Record the organizer and cloud-recording owner in the session manifest.
3. If another company owns the meeting, confirm whether the host can record and retrieve the file before the guest arrives.

Guests can often join in a browser without an account, but the organizer's policy may require email verification or sign-in.
Official reference: [Join a Teams meeting without an account](https://support.microsoft.com/en-us/teams/meetings/join-a-meeting-without-an-account-in-microsoft-teams).

## Capture setup

1. Add a macOS application or window capture source for Teams.
2. Enable its application audio capture.
3. Keep the host microphone as a separate OBS input.
4. Disable any global desktop source that would duplicate the Teams call or host microphone.
5. Route the full mix to track 1, host to track 2, and Teams call audio to track 3.
6. Use the shared layouts from `config/remote-podcast-scenes.json`.

Official reference: [OBS macOS desktop audio capture](https://obsproject.com/kb/macos-desktop-audio-capture-guide).

## Greenroom and recording

1. Admit the guest and confirm microphone, camera, and speaker selection.
2. Confirm recording consent.
3. Start the approved OBS safety/program recording.
4. Start a Teams cloud recording only when the applicable policy and owner are understood.
5. Make a sync clap or spoken marker and record its time in the manifest.

Teams meeting recordings normally land in the organizer's OneDrive or the relevant SharePoint location.
Official reference: [Teams recording storage and permissions](https://learn.microsoft.com/en-us/MicrosoftTeams/tmr-meeting-recording-change).

## Stop and handoff

1. Stop OBS deliberately and confirm the file is playable.
2. Confirm track 1, host track 2, and call track 3 are independently available.
3. Record the Teams cloud file owner and access restrictions when a cloud backup exists.
4. Complete the session manifest and make the second copy.

## Optional NDI enhancement

NDI can expose participant video feeds, but it is not part of the baseline fallback.
It requires an administrator-enabled Teams broadcast-production policy, client production capabilities, an NDI runtime, and an OBS NDI plugin.
Validate that chain separately before relying on it.

Official reference: [Allow broadcast production with NDI](https://learn.microsoft.com/en-us/microsoftteams/use-ndi-in-meetings).

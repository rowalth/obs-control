# Riverside Runbook

Use Riverside as the default for a nontechnical guest.
Riverside isolated tracks are the master; the local OBS program recording is an independent safety/reference file.

## Before the invitation

1. Create the studio session and identify the host account that will own the files.
2. For a restricted corporate network, ask the guest's assistant or IT contact to run the connectivity check.
3. When required, ask IT to allow `*.riverside.fm` on TCP 443/80 and UDP 443/3478.
4. Prepare a host-controlled Teams fallback before sending the invitation.

Official reference: [Prepare for an executive interview](https://support.riverside.fm/hc/en-us/articles/24582326929181-Prepare-for-an-executive-interview).

## Invitation

1. Choose `docs/templates/guest-invitation.en.md` or `guest-invitation.de.md` and
   add the Riverside session link.
2. Send one primary link, not a menu of platform choices.
3. Use the host's direct contact as the fallback path.

## Greenroom and recording

1. Ask the guest to join in Chrome or Edge from a computer when possible.
2. Confirm the correct camera, microphone, and speaker in the lobby.
3. Confirm headphones and recording consent.
4. Start the approved OBS safety recording and the Riverside recording.
5. Confirm Riverside shows the recording and upload indicators for every participant.
6. Record any disconnect or device change in the session manifest.

Official references: [Join as a guest](https://support.riverside.fm/hc/en-us/articles/5252042203037-Join-a-Studio-as-a-Guest) and [Host checklist](https://support.riverside.fm/hc/en-us/articles/5706937784861-Host-checklist-and-tips-Recording-on-computer).

## Stop and handoff

1. Stop the recordings deliberately.
2. Keep every participant's browser or app open until the upload reports success.
3. Download the available isolated audio and video tracks.
4. Preserve the OBS safety recording in the episode folder.
5. Complete `docs/templates/session-manifest.md`, including missing tracks or upload problems.
6. Create the second copy before deleting any local source.

## Failure path

- **Blocked before recording:** move to the prepared Teams fallback; do not ask the guest to diagnose the firewall.
- **Disconnect during recording:** keep recording, restore the guest in Riverside, and mark the reconnect time.
- **Upload incomplete:** leave the guest client open, preserve the OBS safety recording, and record the missing file explicitly.

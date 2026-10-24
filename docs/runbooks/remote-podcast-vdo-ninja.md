# VDO.Ninja Laboratory Runbook

VDO.Ninja is a host-side experiment until it completes three consecutive 60-90 minute qualification sessions.
Do not select it for an ordinary guest session before that gate passes.

## Runtime setup

1. Create a Director room outside the repository.
2. Send the guest one invite link.
3. Obtain one isolated Solo link per guest from the Director view.
4. Add each Solo link to its assigned OBS Browser Source at runtime.
5. Never commit the room name, password, guest link, Director link, or Solo link.

Official reference: [VDO.Ninja Rooms and Solo links](https://docs.vdo.ninja/getting-started/rooms).

## Recording authority

OBS is the primary program and audio recorder.
VDO.Ninja local or remote browser recording is optional backup evidence, not the only master.
Browser recording can consume additional resources, produces WebM, and can be lost after a browser crash.

Official reference: [VDO.Ninja recording options](https://docs.vdo.ninja/guides/options-to-record-streams).

## Qualification record

For each test, record:

- duration;
- guest device and browser;
- reconnect result after a deliberate refresh;
- A/V drift at the end of the timeline;
- CPU or dropped-frame warning;
- OBS file integrity;
- every action required from the guest.

A failed criterion resets the consecutive-pass count.

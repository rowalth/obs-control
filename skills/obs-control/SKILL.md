---
name: obs-control
description: Inspect, configure, and operate a local OBS Studio instance through the obs MCP server. Use for OBS scenes, sources, scene items, transforms, audio, filters, transitions, lower-thirds, recording, streaming, or virtual-camera work.
---

# OBS Control

Use the `obs` MCP tools to work with the OBS instance available to the current
client. OBS is stateful and may already be live, recording, or configured for a
production show.

## Start safely

1. Confirm that OBS is reachable. Read version/status information first.
2. Inspect the current scene collection, active scene, scenes and relevant sources.
3. Report any active stream, recording or virtual camera before proposing changes.
4. Prefer a disposable scene such as `AI-Controlled-Test` for new automation.
5. Only one MCP client should actively control OBS at a time.

If the MCP tools exposed by the installed server do not support a requested OBS
operation, say so. Do not invent tool names or claim that a change succeeded.

## Approval boundary

Obtain explicit user approval in the current request immediately before:

- starting or stopping a stream;
- starting or stopping a recording;
- starting or stopping the virtual camera;
- deleting a scene, source, filter, profile or scene collection;
- replacing a production scene or making a broad, difficult-to-reverse change.

Scene switches and ordinary reversible edits may proceed when they are clearly
part of the user's requested task. Never reveal or request the OBS WebSocket
password; the local launcher supplies it from the host's secret store.

## Change workflow

For every mutation:

1. Read the relevant current state and identify exact names or IDs.
2. Make the smallest reversible change that satisfies the request.
3. Read the state again and verify the intended result.
4. Report what changed and any part that could not be verified visually.

Avoid blind retries. If a tool response is ambiguous, inspect state before
trying again.

## Scenes and lower-thirds

For scene design, first inventory the sources and capabilities available through
the MCP server. Reusable, neutral browser-source templates may live in this
tooling repository. Keep show branding, guest media, recordings, and other
production-specific assets in the owning show/project repository.

For a lower-third:

1. Determine whether the asset is HTML/CSS, image, video or an existing OBS text source.
2. Create or reuse the corresponding source only if the exposed MCP tools support it.
3. Add it to a disposable scene, then set transform, crop, visibility and stacking order.
4. Test show/hide behavior and transitions.
5. Move or reuse the tested source in a production scene only after user review.

The OBS MCP server controls OBS; it does not replace a graphics renderer. Create
missing visual assets with the appropriate design tool, then attach them as OBS
sources.

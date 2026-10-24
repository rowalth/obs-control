# Build the Remote Podcast Lab Collection

This runbook reproduces the public `Remote Podcast Lab` test collection from
`config/remote-podcast-lab.blueprint.json` without publishing a machine-specific OBS
export.

The blueprint was visually validated in OBS 32.2.2 with obs-websocket 5.7.4 on macOS.
Its source types are semantic so an operator can resolve the concrete input kind exposed
by the installed OBS version.

## Safety boundary

Before changing OBS:

1. Confirm recording, streaming, replay buffer, and virtual camera are inactive.
2. Record the current scene collection and program scene.
3. Confirm the active profile uses a 1920×1080 canvas. If it does not, create or switch
   to a disposable profile configured for 1920×1080 before continuing; do not alter a
   production profile for this build.
4. Create a new collection named `Remote Podcast Lab`; do not repurpose a production
   collection.
5. Do not change profile-scoped video or output settings while building the collection.
6. Never insert live guest links, credentials, recordings, or show branding into the
   public blueprint.

Creating a collection may switch OBS to it. OBS may also generate an empty scene named
`Scene`. Keep it unless the operator explicitly approves deletion.

## Resolve the blueprint

- Treat `sources` as the complete reusable-source registry.
- Resolve each `color` source to the first available kind in
  `source_kind_candidates.color`.
- Resolve each `browser` path relative to the repository root at runtime. Never write the
  resulting absolute path back to Git.
- Treat each scene's `items` array as bottom-to-top stacking order.
- An omitted transform means the identity transform.
- Keep every `OVR_CAPTIONS` item disabled until a real caption renderer is configured.

## Build sequence

1. Create every scene named in the blueprint.
2. Create each reusable source once, in the first scene that needs it.
3. Immediately apply every declared source property before adding the source to any
   remaining scene: color, opacity, dimensions, Browser Source dimensions and frame rate,
   restart behavior, and the local file URL resolved from its repository-relative path.
4. Add that source to the remaining scenes in the declared item order.
5. Apply the declared position, scale, and crop values to each scene item.
6. Set `00_PREFLIGHT` as the program scene.
7. Wait for browser-source entrance animations before taking validation screenshots.

Do not change the OBS frame rate as part of this collection build. The blueprint records
30 fps as the recommendation, but frame rate is profile-scoped and can affect other scene
collections.

## Visual verification

Render or inspect at least these scenes at 1920×1080:

- `00_PREFLIGHT` — centered host/guest split and visible lower third;
- `12_HOST_GUEST_50_50` — equal centered crops;
- `13_HOST_GUEST_60_40` — 60/40 centered crops;
- `14_GROUP_GRID` — large host plus two stacked guests;
- `20_SCREEN_SPEAKER` — undistorted screen area plus speaker column;
- `21_SCREEN_PIP` — full screen with bottom-right speaker inset;
- `01_HOLDING` and `90_TECHNICAL_DIFFICULTIES` — title overlay and brand accent.

After verification, re-check that recording, streaming, and virtual camera remain inactive.

## Why the raw OBS export is excluded

OBS scene-collection exports contain internal UUIDs, generated state, and absolute local
browser-source paths. Those values make an export machine-specific and can disclose a
user name or filesystem layout. The blueprint keeps the useful production decisions while
remaining reviewable, portable, and safe to publish.

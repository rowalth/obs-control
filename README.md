# OBS Control

OBS Control is a portable, safety-first toolkit for operating OBS Studio from AI clients and for building a reliable remote-podcast production system.

It combines three layers:

- a local launcher for [`royshil/obs-mcp`](https://github.com/royshil/obs-mcp);
- reusable operating rules for Codex and Claude;
- a remote-podcast kit with a reproducible OBS lab blueprint, browser overlays, preflight
  checks, and Riverside, Teams, and VDO.Ninja runbooks.

The guest never interacts with OBS.
The host chooses one guest platform and runs the production machinery locally.

## Status

The repository is an early public v0.1.
The portable launcher, production contracts, validated lab blueprint, overlays, validators,
and operator runbooks are available. Live OBS changes and real guest qualification remain
controlled operator steps because they affect a stateful production application.

## Architecture

```text
Codex / Claude Code / Claude Desktop
                 |
                 | MCP over stdio
                 v
 scripts/obs-mcp-launcher
                 |
                 | OBS WebSocket on localhost:4455
                 v
               OBS Studio

Guest link: Riverside | Teams | VDO.Ninja
                 |
                 v
      OBS scenes + audio tracks
                 |
                 v
      Recoverable editor handoff
```

OBS remains the system that owns scenes, sources, filters, recordings, and streams.
The MCP server runs locally and connects to `ws://127.0.0.1:4455` by default.

## Remote-podcast modes

| Mode | Role | Recording authority |
|---|---|---|
| Riverside | Default for nontechnical guests | Riverside isolated tracks are the master; OBS is the safety/program reference |
| Microsoft Teams | Corporate fallback | OBS program and separated host/call audio; Teams cloud recording is an optional backup |
| VDO.Ninja | Laboratory mode | OBS is primary; promotion requires three consecutive qualification sessions |
| Jitsi Meet | Deferred candidate | Not implemented in v0.1; recording authority will be defined during later qualification |

The implemented and laboratory modes are exclusive for a session.
A guest is never asked to join multiple platforms to make the production setup work.

Jitsi Meet is recorded as a future option only. Before implementation it must be
qualified for corporate-browser access, guest simplicity, OBS capture, audio separation,
recording ownership, and recovery behavior.

## Prerequisites

- OBS Studio 31 or newer
- Node.js 16 or newer with `npx`
- Python 3.9 or newer for validation and preflight scripts
- OBS WebSocket enabled under **Tools > WebSocket Server Settings**
- Local WebSocket authentication enabled on port `4455`

## Install the local MCP launcher

Clone the repository and set its absolute location for the commands below:

```sh
OBS_CONTROL_DIR="/absolute/path/to/obs-control"
```

On macOS, store the OBS WebSocket password in Keychain.
The command prompts securely and does not echo the value:

```sh
security add-generic-password -U -a "$USER" -s "obs-mcp.websocket" -w
```

Register the launcher with Codex:

```sh
codex mcp add obs -- "$OBS_CONTROL_DIR/scripts/obs-mcp-launcher"
codex mcp get obs
```

Register it with Claude Code:

```sh
claude mcp add --scope user obs -- "$OBS_CONTROL_DIR/scripts/obs-mcp-launcher"
claude mcp get obs
```

Claude Desktop can use the template at `config/claude-desktop.example.json` after replacing `/absolute/path/to/obs-control`.

The launcher supports these optional overrides:

- `OBS_WEBSOCKET_URL` — defaults to `ws://127.0.0.1:4455`;
- `OBS_WEBSOCKET_PASSWORD` — supplies the password through the current process environment;
- `OBS_MCP_KEYCHAIN_SERVICE` and `OBS_MCP_KEYCHAIN_ACCOUNT` — select another macOS Keychain entry;
- `OBS_MCP_NPX` — points to another `npx` executable.

On Linux, supply `OBS_WEBSOCKET_PASSWORD` through the machine's secret manager.
Do not expose port `4455` directly to the public internet.

## Validate the repository

Run the static contract and secret checks:

```sh
scripts/remote-podcast-validate
```

Run an offline production preflight:

```sh
REMOTE_PODCAST_RECORDING_DIR="$HOME/Movies/podcast" \
  scripts/remote-podcast-preflight --offline
```

Run the test suite:

```sh
PYTHONDONTWRITEBYTECODE=1 \
  python3 -m unittest discover -s tests/remote-podcast -p 'test_*.py'
```

The offline checks do not mutate OBS, start a recording, or contact a guest platform.

## Reproduce the OBS lab collection

`config/remote-podcast-lab.blueprint.json` captures the public-safe source definitions,
stacking order, crops, scales, positions, and disabled caption placeholders that were
validated in the live `Remote Podcast Lab` collection.

Follow `docs/runbooks/build-remote-podcast-lab.md` to rebuild it safely. The repository
intentionally excludes the raw OBS export because it contains internal UUIDs and absolute
machine paths.

## Build a show from the toolkit

1. Read `docs/architecture/remote-podcast-studio.md`.
2. Choose the English or German guest invitation under `docs/templates/guest-invitation.md`.
3. Copy `docs/templates/show-brand-handoff.md` into the owning show repository and resolve its asset slots there.
4. Use `config/remote-podcast-scenes.json` as the canonical scene/component manifest and
   `config/remote-podcast-lab.blueprint.json` as the reproducible layout contract.
5. Resolve the browser overlay paths against the local repository at runtime.
6. Follow the relevant runbook under `docs/runbooks/`.
7. Build and verify scenes in a disposable collection before promoting them to production.

Show logos, fonts, named lower thirds, final intro/outro media, episode data, guest links, and recordings do not belong in this repository.

## Safety model

The shared `skills/obs-control/` skill requires state inspection before mutation and explicit approval before:

- starting or stopping a stream, recording, or virtual camera;
- deleting scenes, sources, profiles, filters, or collections;
- replacing a production scene collection.

Use exactly one MCP client to control OBS at a time.

## Contributing

See `CONTRIBUTING.md` for the verification and scope rules.
Report security issues through the private process in `SECURITY.md`, not through a public issue.

## License and provenance

This repository is licensed under the MIT License.

It launches but does not vendor [`royshil/obs-mcp`](https://github.com/royshil/obs-mcp), which is distributed under GPL-2.0.
The launcher currently pins `obs-mcp@1.1.0` so upgrades remain deliberate and testable.

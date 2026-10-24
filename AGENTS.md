# OBS Control — shared local tooling

This repository owns the reusable local OBS integration for Codex and Claude,
plus generic production contracts, overlays and runbooks for remote podcasts.
It wraps [royshil/obs-mcp](https://github.com/royshil/obs-mcp) with one launcher
and keeps the operating system separate from show-specific branding.

## Working boundary

- Keep generic launchers, scene contracts, overlays, runbooks and the reusable `obs-control` skill here.
- Keep show-specific scenes, lower-thirds, brand assets and runbooks in their owning project repos.
- Never store the OBS WebSocket password, tokens, `.env` files or client-specific secrets in Git.
- The macOS launcher reads the password from Keychain service `obs-mcp.websocket` by default.
- Treat OBS as a local stateful application. Inspect current state before changing it.

## Safety rules

- Never start or stop a stream, recording or virtual camera without explicit user approval in the current request.
- Never delete scenes, sources, filters, profiles or scene collections without explicit approval.
- Build and test automation in a disposable scene or scene collection first.
- Prefer idempotent changes and verify the resulting OBS state after each mutation.
- Only one MCP client should actively control OBS at a time.

## Verification

```sh
zsh -n scripts/obs-mcp-launcher
OBS_WEBSOCKET_PASSWORD=test OBS_MCP_NPX=/usr/bin/true scripts/obs-mcp-launcher
scripts/remote-podcast-validate
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests/remote-podcast -p 'test_*.py'
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" skills/obs-control
```

Live verification additionally requires OBS to be open with its WebSocket server enabled.

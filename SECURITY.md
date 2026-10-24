# Security Policy

## Supported versions

Only the latest revision of the default branch is supported during the v0.x phase.

## Reporting a vulnerability

Do not open a public issue for a suspected vulnerability or exposed credential.
Use the repository's private GitHub security-advisory form under **Security > Advisories > New draft advisory**.

Include the affected file or component, reproduction steps, likely impact, and whether a credential may already have been exposed.
Do not include a real OBS WebSocket password, guest URL, room password, or access token in the report.

## Secret handling

The repository must never contain:

- OBS WebSocket passwords;
- Riverside, Teams, or VDO.Ninja guest or director links;
- room names paired with passwords;
- `.env` files or access tokens;
- raw recordings or personally identifying episode manifests.

The macOS launcher reads its password from Keychain by default.
Other platforms must supply it through a local secret manager.

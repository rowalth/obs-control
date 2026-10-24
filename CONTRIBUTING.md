# Contributing

Contributions should improve the reusable OBS integration or the generic remote-podcast system.
Show-specific scenes, branding, guest information, and recordings belong in another repository.

Before opening a pull request:

1. Run `zsh -n scripts/obs-mcp-launcher`.
2. Run `scripts/remote-podcast-validate`.
3. Run `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests/remote-podcast -p 'test_*.py'`.
4. Confirm that no absolute personal path, credential, guest URL, or media recording is present.

Live OBS changes must be developed in a disposable scene collection.
Never start or stop recording, streaming, or the virtual camera as part of an automated test.

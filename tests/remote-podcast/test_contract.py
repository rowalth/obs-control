from __future__ import annotations

import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import unittest


REPO = Path(__file__).resolve().parents[2]


class RepositoryContractTests(unittest.TestCase):
    def test_portable_files_do_not_contain_a_personal_home_path(self) -> None:
        candidates = [
            REPO / "README.md",
            REPO / "AGENTS.md",
            REPO / "scripts" / "obs-mcp-launcher",
            REPO / "config" / "codex.example.toml",
            REPO / "config" / "claude-desktop.example.json",
        ]

        for path in candidates:
            personal_home = "/Users/" + "rwa/"
            self.assertNotIn(personal_home, path.read_text(), path)

    def test_default_contract_is_machine_readable(self) -> None:
        config = json.loads(
            (REPO / "config" / "remote-podcast.defaults.json").read_text()
        )

        self.assertEqual(config["video"], {"width": 1920, "height": 1080, "fps": 30})
        self.assertEqual(config["audio"]["sample_rate_hz"], 48000)
        self.assertEqual(
            [track["id"] for track in config["audio"]["tracks"]],
            [1, 2, 3, 4, 5],
        )
        self.assertEqual(config["modes"]["default"], "riverside")
        self.assertEqual(config["modes"]["vdo_ninja"]["status"], "laboratory")

    def test_scene_manifest_references_declared_components(self) -> None:
        manifest = json.loads(
            (REPO / "config" / "remote-podcast-scenes.json").read_text()
        )
        component_names = set(manifest["components"])
        scene_names = {scene["name"] for scene in manifest["scenes"]}

        self.assertEqual(len(scene_names), len(manifest["scenes"]))
        self.assertIn("00_PREFLIGHT", scene_names)
        self.assertIn("99_END_CARD", scene_names)
        for scene in manifest["scenes"]:
            self.assertTrue(set(scene["components"]) <= component_names, scene["name"])

    def test_lab_blueprint_is_portable_and_matches_scene_contract(self) -> None:
        manifest = json.loads(
            (REPO / "config" / "remote-podcast-scenes.json").read_text()
        )
        blueprint = json.loads(
            (REPO / "config" / "remote-podcast-lab.blueprint.json").read_text()
        )
        manifest_scenes = {scene["name"]: scene for scene in manifest["scenes"]}
        blueprint_scenes = {scene["name"]: scene for scene in blueprint["scenes"]}

        self.assertEqual(set(blueprint["sources"]), set(manifest["components"]))
        self.assertEqual(set(blueprint_scenes), set(manifest_scenes))

        for name, definition in blueprint["sources"].items():
            if definition["type"] != "browser":
                continue
            path = Path(definition["path"])
            self.assertFalse(path.is_absolute(), name)
            self.assertTrue((REPO / path).is_file(), name)

        for name, scene in blueprint_scenes.items():
            item_sources = [item["source"] for item in scene["items"]]
            self.assertEqual(item_sources, manifest_scenes[name]["components"], name)
            for item in scene["items"]:
                if item["source"] == "OVR_CAPTIONS":
                    self.assertFalse(item["enabled"], name)

        fifty_fifty = {
            item["source"]: item for item in blueprint_scenes["12_HOST_GUEST_50_50"]["items"]
        }
        self.assertEqual(fifty_fifty["SRC_HOST"]["transform"]["crop_left"], 480)
        self.assertEqual(fifty_fifty["SRC_GUEST_1"]["transform"]["position_x"], 960)

        screen_pip = {
            item["source"]: item for item in blueprint_scenes["21_SCREEN_PIP"]["items"]
        }
        self.assertEqual(screen_pip["SRC_HOST"]["transform"]["scale_x"], 0.25)
        self.assertEqual(screen_pip["SRC_HOST"]["transform"]["position_x"], 1400)

    def test_overlays_use_text_content_and_safe_area_constraints(self) -> None:
        for overlay in ("lower-third", "episode-title"):
            script = (REPO / "overlays" / overlay / "app.js").read_text()
            styles = (REPO / "overlays" / overlay / "style.css").read_text()

            self.assertIn("textContent", script)
            self.assertNotIn("innerHTML", script)
            self.assertIn("--safe-area", styles)
            self.assertIn("overflow-wrap", styles)

    def test_runbooks_preserve_master_and_fallback_rules(self) -> None:
        riverside = (REPO / "docs" / "runbooks" / "remote-podcast-riverside.md").read_text()
        teams = (REPO / "docs" / "runbooks" / "remote-podcast-teams.md").read_text()
        invitations = {
            language: (
                REPO / "docs" / "templates" / f"guest-invitation.{language}.md"
            ).read_text()
            for language in ("en", "de")
        }
        normalized_invitations = {
            language: " ".join(invitation.lower().split())
            for language, invitation in invitations.items()
        }

        self.assertIn("isolated tracks are the master", riverside.lower())
        self.assertIn("application audio", teams.lower())
        self.assertIn("one primary link", normalized_invitations["en"])
        self.assertIn("einen primären link", normalized_invitations["de"])
        self.assertIn("allow camera and microphone access", normalized_invitations["en"])
        self.assertIn("zugriff auf kamera und mikrofon", normalized_invitations["de"])
        placeholders = {
            language: set(re.findall(r"\{\{[A-Z_]+\}\}", invitation))
            for language, invitation in invitations.items()
        }
        self.assertEqual(placeholders["en"], placeholders["de"])
        for invitation in invitations.values():
            self.assertIn("{{PRIMARY_LINK}}", invitation)
            self.assertIn("{{HOST_PHONE}}", invitation)
            self.assertNotIn("VDO.Ninja", invitation)
            self.assertNotIn("OBS", invitation)

    def test_repository_validator_passes_the_checkout(self) -> None:
        result = subprocess.run(
            [str(REPO / "scripts" / "remote-podcast-validate"), "--root", str(REPO)],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_repository_validator_flags_runtime_secrets(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "config").mkdir()
            (root / "config" / "runtime.txt").write_text(
                "room_" + "password=do-not-commit\n"
                + "https://vdo.ninja/?" + "room=private-room&password=secret\n"
            )
            result = subprocess.run(
                [str(REPO / "scripts" / "remote-podcast-validate"), "--root", str(root)],
                check=False,
                capture_output=True,
                text=True,
            )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("possible runtime secret", result.stdout.lower())

    def test_offline_preflight_accepts_a_writable_recording_directory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            environment = os.environ.copy()
            environment["OBS_MCP_NPX"] = "/usr/bin/true"
            environment["REMOTE_PODCAST_RECORDING_DIR"] = directory
            environment["REMOTE_PODCAST_MIN_FREE_GB"] = "0"
            result = subprocess.run(
                [str(REPO / "scripts" / "remote-podcast-preflight"), "--offline"],
                check=False,
                capture_output=True,
                text=True,
                env=environment,
            )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("offline preflight passed", result.stdout.lower())


if __name__ == "__main__":
    unittest.main()

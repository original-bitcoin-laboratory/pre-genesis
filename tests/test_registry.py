import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_checksum_registry_is_nov08_with_two_artifacts():
    data = json.loads((ROOT / "manifests" / "EXPECTED_CHECKSUMS.json").read_text())
    assert data["schema"] == 1
    assert len(data["artifacts"]) == 2
    assert {a["profile"] for a in data["artifacts"]} == {"OBL-NOV08"}


def test_all_artifact_urls_use_https():
    data = json.loads((ROOT / "manifests" / "EXPECTED_CHECKSUMS.json").read_text())
    assert all(a["url"].startswith("https://") for a in data["artifacts"])

import json
import os
import subprocess
import hashlib
from pathlib import Path
import jsonschema

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts" / "day5"
SCHEMA = ROOT / "schemas" / "day5_summary.schema.json"


def jload(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def test_env_vars():
    assert os.environ.get("STUDENT_TOKEN"), "STUDENT_TOKEN not set"
    assert os.environ.get("STUDENT_NAME"),  "STUDENT_NAME not set"
    assert os.environ.get("STUDENT_GROUP"), "STUDENT_GROUP not set"


def test_required_artifacts_exist():
    required = [
        ART / "yang" / "ietf-interfaces.yang",
        ART / "yang" / "pyang_version.txt",
        ART / "yang" / "pyang_tree.txt",
        ART / "webex" / "me.json",
        ART / "webex" / "rooms_list.json",
        ART / "webex" / "room_create.json",
        ART / "webex" / "message_post.json",
        ART / "webex" / "messages_list.json",
        ART / "pt" / "external_access_check.json",
        ART / "pt" / "serviceTicket.txt",
        ART / "pt" / "network_devices.json",
        ART / "pt" / "hosts.json",
    ]
    for f in required:
        assert f.exists(), f"Missing: {f}"
        assert f.stat().st_size > 0, f"Empty: {f}"


def test_day5_summary_and_schema():
    env = os.environ.copy()
    r = subprocess.run(
        ["python3", "src/day5_summary_builder.py"],
        cwd=str(ROOT), env=env,
        capture_output=True, text=True
    )
    assert r.returncode in (0, 2), r.stderr
    assert (ART / "summary.json").exists()

    summary = jload(ART / "summary.json")
    schema = jload(SCHEMA)
    jsonschema.validate(instance=summary, schema=schema)


def test_token_hash8_correct():
    summary = jload(ART / "summary.json")
    token = os.environ["STUDENT_TOKEN"]
    expected = hashlib.sha256(token.encode()).hexdigest()[:8]
    assert summary["student"]["token_hash8"] == expected


def test_yang_tree_has_interfaces():
    summary = jload(ART / "summary.json")
    assert summary["checks"]["yang_tree_has_interfaces"] is True

    tree = (ART / "yang" / "pyang_tree.txt").read_text()
    assert "+--rw interfaces" in tree
    assert "enabled" in tree


def test_webex_room_title_contains_hash8():
    summary = jload(ART / "summary.json")
    assert summary["checks"]["webex_room_title_contains_hash8"] is True

    token = os.environ["STUDENT_TOKEN"]
    room = jload(ART / "webex" / "room_create.json")
    title = room.get("title", "")
    assert token in title or summary["student"]["token_hash8"] in title


def test_webex_message_contains_hash8():
    summary = jload(ART / "summary.json")
    token = os.environ["STUDENT_TOKEN"]
    token_hash8 = summary["student"]["token_hash8"]

    msg = jload(ART / "webex" / "message_post.json")
    text = msg.get("text", "") + msg.get("markdown", "")
    assert token in text or token_hash8 in text


def test_pt_empty_ticket_seen():
    summary = jload(ART / "summary.json")
    assert summary["checks"]["pt_empty_ticket_seen"] is True

    ext = (ART / "pt" / "external_access_check.json").read_text().lower()
    assert "empty ticket" in ext


def test_pt_network_devices_and_hosts():
    summary = jload(ART / "summary.json")
    assert summary["checks"]["pt_network_devices_ok"] is True
    assert summary["checks"]["pt_hosts_ok"] is True

    net = (ART / "pt" / "network_devices.json").read_text()
    hosts = (ART / "pt" / "hosts.json").read_text()
    assert '"version": "1.0"' in net
    assert '"version": "1.0"' in hosts

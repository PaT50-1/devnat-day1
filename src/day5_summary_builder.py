import json
import hashlib
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts" / "day5"
OUT = ART / "summary.json"

SCHEMA_VERSION = "5.0"


def sha256_file(p: Path) -> str:
    if not p.exists():
        return ""
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read_text(p: Path) -> str:
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8", errors="ignore")


def read_json(p: Path) -> dict:
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def main():
    student_token = os.environ.get("STUDENT_TOKEN", "")
    student_name = os.environ.get("STUDENT_NAME", "")
    student_group = os.environ.get("STUDENT_GROUP", "")

    if not student_token:
        print("ERROR: STUDENT_TOKEN not set", file=sys.stderr)
        sys.exit(1)

    token_hash8 = hashlib.sha256(student_token.encode()).hexdigest()[:8]

    # YANG checks
    yang_dir = ART / "yang"
    pyang_tree = yang_dir / "pyang_tree.txt"
    pyang_tree_text = read_text(pyang_tree)
    yang_ok = "+--rw interfaces" in pyang_tree_text

    # Webex checks
    webex_dir = ART / "webex"
    room_create = read_json(webex_dir / "room_create.json")
    room_title = room_create.get("title", "")
    webex_room_has_hash = student_token in room_title or token_hash8 in room_title
    webex_ok = webex_room_has_hash and (webex_dir / "me.json").exists()

    # PT checks
    pt_dir = ART / "pt"
    ext_check_text = read_text(pt_dir / "external_access_check.json")
    empty_ticket_seen = "empty ticket" in ext_check_text.lower()

    net_dev_text = read_text(pt_dir / "network_devices.json")
    hosts_text = read_text(pt_dir / "hosts.json")
    pt_devices_ok = '"version": "1.0"' in net_dev_text
    pt_hosts_ok = '"version": "1.0"' in hosts_text
    pt_ok = empty_ticket_seen and pt_devices_ok and pt_hosts_ok

    validation_passed = yang_ok and webex_ok and pt_ok

    summary = {
        "schema_version": SCHEMA_VERSION,
        "student": {
            "token": student_token,
            "token_hash8": token_hash8,
            "name": student_name,
            "group": student_group,
        },
        "yang": {
            "ok": yang_ok,
            "evidence_sha": sha256_file(pyang_tree),
        },
        "webex": {
            "ok": webex_ok,
            "room_title_contains_hash8": webex_room_has_hash,
            "room_title": room_title,
            "evidence_sha": sha256_file(webex_dir / "room_create.json"),
        },
        "pt": {
            "ok": pt_ok,
            "empty_ticket_seen": empty_ticket_seen,
            "network_devices_ok": pt_devices_ok,
            "hosts_ok": pt_hosts_ok,
            "evidence_sha": sha256_file(pt_dir / "external_access_check.json"),
        },
        "bonus": {
            "optional_ok": False,
            "evidence_sha": "",
        },
        "validation_passed": validation_passed,
        "checks": {
            "yang_tree_has_interfaces": yang_ok,
            "webex_room_title_contains_hash8": webex_room_has_hash,
            "pt_empty_ticket_seen": empty_ticket_seen,
            "pt_network_devices_ok": pt_devices_ok,
            "pt_hosts_ok": pt_hosts_ok,
        },
    }

    ART.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(summary, indent=4, ensure_ascii=False), encoding="utf-8")
    print(f"summary.json written to {OUT}")
    print(f"token_hash8: {token_hash8}")
    print(f"yang_ok: {yang_ok}")
    print(f"webex_ok: {webex_ok}")
    print(f"pt_ok: {pt_ok}")
    print(f"validation_passed: {validation_passed}")

    sys.exit(0 if validation_passed else 2)


if __name__ == "__main__":
    main()

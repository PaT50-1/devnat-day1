# Day 5 Report — Module 8 Capstone

## 1) Student
- Name: Ostrovenko Pavel
- Group: IB-23-5B
- Token: D1-IB-23-5b-14-D3B8   
- Repo: https://github.com/PaT50-1/devnat-day1

## 2) YANG (8.3.5)
- Evidence files:
  - artifacts/day5/yang/ietf-interfaces.yang - Yes
  - artifacts/day5/yang/pyang_version.txt - Yes
  - artifacts/day5/yang/pyang_tree.txt - Yes

## 3) Webex (8.6.7)
- Room title contains token_hash8: Yes
- Message text contains token_hash8: Yes
- Evidence files:
  - me.json / rooms_list.json / room_create.json / message_post.json / messages_list.json - Yes

## 4) Packet Tracer Controller REST (8.8.3)
- external_access_check contains “empty ticket”: Yes
- serviceTicket saved: Yes
- Evidence files:
  - external_access_check.json / network_devices.json / hosts.json - Yes
  - postman_collection.json / postman_environment.json - Yes
  - pt_internal_output.txt - Yes

## 5) Commands output (paste exact)
```text
python src/day5_summary_builder.py:

summary.json written to /home/devasc/devnet-day1-IB-23-5B-Ostrovenko/artifacts/day5/summary.json
token_hash8: cc1a8214
yang_ok: True
webex_ok: True
pt_ok: True
validation_passed: True

pytest -q:

=============== test session starts ================
platform linux -- Python 3.8.2, pytest-4.6.9, py-1.8.1, pluggy-0.13.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/devasc/devnet-day1-IB-23-5B-Ostrovenko
plugins: Faker-4.1.1
collected 9 items                                  

tests/test_day5_module8.py::test_env_vars PASSED [ 11%]
tests/test_day5_module8.py::test_required_artifacts_exist PASSED [ 22%]
tests/test_day5_module8.py::test_day5_summary_and_schema PASSED [ 33%]
tests/test_day5_module8.py::test_token_hash8_correct PASSED [ 44%]
tests/test_day5_module8.py::test_yang_tree_has_interfaces PASSED [ 55%]
tests/test_day5_module8.py::test_webex_room_title_contains_hash8 PASSED [ 66%]
tests/test_day5_module8.py::test_webex_message_contains_hash8 PASSED [ 77%]
tests/test_day5_module8.py::test_pt_empty_ticket_seen PASSED [ 88%]
tests/test_day5_module8.py::test_pt_network_devices_and_hosts PASSED [100%]

============= 9 passed in 0.11 seconds =============

```
## 6) Problems & fixes (at least 1)
- Problem: Programming tab was empty with no New button — Python projects unavailable in version 7.4.0T installed on DEVASC VM
- Fix: Opened the .pka file on Windows with Packet Tracer where the Programming tab works correctly
- Proof: Part 6 completed, console output saved to pt_internal_output.txt
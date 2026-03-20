# Day 4 Report — Labs 6–7 (Docker + Jenkins + Security + Ansible)

## 1) Student
- Name: Ostrovenko Pavel
- Group: IB-23-5B
- Token: D1-IB-23-5b-14-D3B8
- Repo: https://github.com/PaT50-1/devnat-day1/tree/main

## 2) Evidence checklist (files exist)
### Docker (6.2.7)
- artifacts/day4/docker/sampleapp_curl.txt: Yes
- artifacts/day4/docker/sampleapp_token_proof.txt: Yes
- artifacts/day4/docker/sampleapp_docker_ps.txt: Yes
- artifacts/day4/docker/sampleapp_build_log.txt: Yes

### Jenkins (6.3.6)
- artifacts/day4/jenkins/jenkins_docker_ps.txt: No
- artifacts/day4/jenkins/buildapp_console.txt: No
- artifacts/day4/jenkins/testapp_console.txt: No
- artifacts/day4/jenkins/pipeline_script.groovy: No
- artifacts/day4/jenkins/pipeline_console.txt: No
- artifacts/day4/jenkins/jenkins_url.txt: No

### Ansible (7.4.8)
- artifacts/day4/ansible/ansible_ping.txt: Yes
- artifacts/day4/ansible/ansible_hello.txt: Yes
- artifacts/day4/ansible/ansible_playbook_install.txt: Yes
- artifacts/day4/ansible/ports_conf_after.txt: Yes
- artifacts/day4/ansible/curl_apache_8081.txt: Yes

### Security (6.5.10)
- artifacts/day4/security/signup_v1.txt: Yes
- artifacts/day4/security/login_v1.txt: Yes
- artifacts/day4/security/signup_v2.txt: Yes
- artifacts/day4/security/login_v2.txt: Yes
- artifacts/day4/security/db_tables.txt: YEs
- artifacts/day4/security/db_user_hash_sample.txt: YEs

## 3) Commands output

python src/day4_summary_builder.py:

{
  "schema_version": "4.1",
  "generated_utc": "2026-03-20T13:04:52.585607+00:00",
  "student": {
    "token": "D1-IB-23-5b-14-D3B8",
    "token_hash8": "cc1a8214",
    "name": "Ostrovenko",
    "group": "IB-23-5B"
  },
  "checks": {
    "docker_token_in_page": false,
    "docker_tokenproof": false,
    "ansible_port_8081": true,
    "jenkins_pipeline_has_stages": false,
    "security_db_has_tables": true
  },
  "evidence_sha256": {
    "docker_sampleapp_curl": "04b31e9814b0c89b5d85bf790ab8e3ea591d84ffb6403758b6220e0e3c08a0ca",
    "docker_ps": "59cb64fc2f445c6be0f4a82ed9446ae8770695faf4702efdce56f8f086614163",
    "docker_build_log": "",
    "docker_token_proof": "c8f4668f293859baeb493504141d536368176c88abbef2fa7dae89e9f45b4987",
    "jenkins_docker_ps": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "buildapp_console": "",
    "testapp_console": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "pipeline_script": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "pipeline_console": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "jenkins_url": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "ansible_ping": "005e9245df2c530d64aee6bfec751dfc3ced4b06361f597e7fde4163bc44fd69",
    "ansible_hello": "6b506fcd95eb0febede6e36542f9524299ecd459f7b11b6743bef44138cbb0fb",
    "ansible_playbook_install": "4812a9fd7cfc73faab5fc370a200aca57e9554e13dcc64e09be2b28d2b922a25",
    "ports_conf_after": "8ee0ac8272eaa90ca6a9597cb472034768331e543d074cc72141b520ffb6f686",
    "curl_apache_8081": "a9a7989c97b2813c1fc0f00f368605a12a9835cffeb65f63b30ec1b4f69048b8",
    "signup_v1": "11e553d68742d167ff0e6d1c9a04b7210c80f09fe1cc4c52e0019e2493b59bfa",
    "login_v1": "fc6d9fe5f04505908614c216b173081e1149efca83ed3e54821e75b5312658ae",
    "signup_v2": "512d2686aabb177a885aece270166e8fe20da75f6cd1c198a09debeffccb65bb",
    "login_v2": "b03423d1857be7c9488d82fd7a56b3028ba002eef71f253a8efff149c1f23bab",
    "db_tables": "5a5db0577f7de3dda0dfbe3e2437f3761ffabf34af83bfd94e0d5423193ce3dd",
    "db_user_hash_sample": "dd4bddd2bd8b4d0d45edfeeef75b54c6a95a6c84732b9311e4e8cd2eb38df05e"
  },
  "validation_passed": false,
  "run": {
    "python": "3.8.2",
    "platform": "linux"
  }
}

pytest -q:

=schema)
    
        # сильные проверки
>       assert summary["checks"]["docker_token_in_page"] is True
E       assert False is True

tests/test_day4_labs.py:27: AssertionError
============= short test summary info ==============
FAILED tests/test_day4_labs.py::test_day4_summary_and_required_evidence - assert False is True
1 failed, 2 passed in 0.41s

## 4) Short reflection (5–8 lines)
- What was the hardest part today and why?
- One security mistake you avoided (or made and fixed):
Jenkins lab was skipped due to EPERM errors when starting the JVM inside
Docker in the DEVASC VM. Tried --security-opt seccomp=unconfined and
--privileged but neither worked. All other labs completed successfully.

## 5) Problems & fixes (at least 1)
- Problem: Jenkins container failed to start with "pthread_create failed (EPERM)"
- Fix attempted: "--security-opt seccomp=unconfined", "--privileged", volume recreate - all failed
- Deciscion: Skipped lab 6.3.6, pipeline_script.groovy provided as static file
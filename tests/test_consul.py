import pytest
import requests


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


@pytest.fixture()
def Hostname(TestinfraBackend):
    return TestinfraBackend.get_hostname()


def test_consul_user(User, Group, AnsibleDefaults):
    assert Group(AnsibleDefaults["consul_group"]).exists
    assert User(AnsibleDefaults["consul_user"]).exists
    assert User(AnsibleDefaults["consul_user"]).group == AnsibleDefaults["consul_group"]


def test_consul_conf(File, AnsibleDefaults, Hostname):
    conf_dir = File(AnsibleDefaults["consul_configdir"])
    data_dir = File(AnsibleDefaults["consul_datadir"])
    bin_dir = File(AnsibleDefaults["consul_bindir"])

    assert conf_dir.exists
    assert conf_dir.is_directory
    assert conf_dir.user == AnsibleDefaults["consul_user"]
    assert conf_dir.group == AnsibleDefaults["consul_group"]

    conf = File(AnsibleDefaults["consul_configdir"] + "/consul.json")
    assert conf.exists
    assert conf.is_file
    assert conf.user == AnsibleDefaults["consul_user"]
    assert conf.group == AnsibleDefaults["consul_group"]
    if "server" in Hostname:
        assert conf.contains("\"server\": true")
    else:
        assert conf.contains("\"server\": false")
    assert data_dir.exists
    assert data_dir.is_directory
    assert data_dir.user == AnsibleDefaults["consul_user"]
    assert data_dir.group == AnsibleDefaults["consul_group"]

    assert bin_dir.exists
    assert bin_dir.is_directory
    assert bin_dir.user == AnsibleDefaults["consul_user"]
    assert bin_dir.group == AnsibleDefaults["consul_group"]


def test_consul_executable(File, Command, AnsibleDefaults):
    consul = File(AnsibleDefaults["consul_bindir"] + "/consul")
    assert consul.user == AnsibleDefaults["consul_user"]
    assert consul.group == AnsibleDefaults["consul_group"]
    assert File("/usr/bin/consul").exists
    assert File("/usr/bin/consul").is_symlink
    assert File("/usr/bin/consul").linked_to == AnsibleDefaults["consul_bindir"] + "/consul"
    consul_version = Command("consul --version")
    assert consul_version.rc is 0
    assert "Consul v" + AnsibleDefaults["consul_version"] in consul_version.stdout


def test_consul_service(File, Service, Socket, Interface, Hostname):
    assert File("/etc/systemd/system/consul.service").exists
    assert Service("consul").is_enabled
    assert Service("consul").is_running
    if "server" in Hostname:
        assert Socket("tcp://" + Interface("eth1").addresses[0] + ":8300").is_listening
        assert Socket("tcp://:::8500").is_listening
    else:
        assert Socket("tcp://127.0.0.1:8500").is_listening
    assert Socket("tcp://127.0.0.1:8600").is_listening


def test_consul_server(Interface, Hostname):
    if "server" in Hostname:
        response = requests.get("http://" + Interface("eth1").addresses[0] + ":8500/ui")
        assert response.status_code == 200


def test_consul_acls(File, Interface, Hostname, AnsibleDefaults):
    if "server" in Hostname:
        acl_conf = File(AnsibleDefaults["consul_configdir"] + "/master.json")
        acl_conf.exists
        acl_conf.user == AnsibleDefaults["consul_user"]
        acl_conf.group == AnsibleDefaults["consul_group"]
        url_forbidden = "http://" + Interface("eth1").addresses[0] + ":8500/v1/acl/list"
        response_forbidden = requests.get(url_forbidden)
        assert response_forbidden.status_code == 403
        token = AnsibleDefaults["consul_acl_master_token"]
        url_auth = "http://" + Interface("eth1").addresses[0] + ":8500/v1/acl/list?token=" + token
        response_auth = requests.get(url_auth)
        assert response_auth.status_code == 200

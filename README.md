# docker-splunk-silicon: For Aarch64 Apple M1 & M2 
# From
# Docker-Splunk: Containerizing Splunk Enterprise

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)&nbsp;
[![GitHub release](https://img.shields.io/github/v/tag/splunk/docker-splunk?sort=semver&label=Version)](https://github.com/splunk/docker-splunk/releases)

Welcome to the unofficial Splunk Arm repository of Dockerfiles for building Splunk Enterprise and Splunk Universal Forwarder images for containerized deployments.

----
Tested Running on Redhat (aarch64) 8 only.  
Passes the first 8 tests

To build make sure you have python and pip setup on your mac

Go to the base folder and enter 

```bash
export PATH=$PATH:~/Library/Python/3.9/bin
make test_redhat8
```

Once your get passed the build stage you'll see the tests running below:

```bash
tests/test_single_splunk_image.py::TestDockerSplunk::test_compose_1so_custombuild 
tests/test_single_splunk_image.py::TestDockerSplunk::test_splunk_entrypoint_help 
[gw0] PASSED tests/test_single_splunk_image.py::TestDockerSplunk::test_splunk_entrypoint_help 
tests/test_single_splunk_image.py::TestDockerSplunk::test_splunk_scloud 
[gw0] PASSED tests/test_single_splunk_image.py::TestDockerSplunk::test_splunk_scloud 
tests/test_single_splunk_image.py::TestDockerSplunk::test_splunk_ulimit 
[gw0] PASSED tests/test_single_splunk_image.py::TestDockerSplunk::test_splunk_ulimit 
tests/test_single_splunk_image.py::TestDockerSplunk::test_splunk_entrypoint_create_defaults 
[gw0] PASSED tests/test_single_splunk_image.py::TestDockerSplunk::test_splunk_entrypoint_create_defaults 
tests/test_single_splunk_image.py::TestDockerSplunk::test_splunk_entrypoint_start_no_password 
[gw0] PASSED tests/test_single_splunk_image.py::TestDockerSplunk::test_splunk_entrypoint_start_no_password 
tests/test_single_splunk_image.py::TestDockerSplunk::test_splunk_entrypoint_start_no_accept_license 
[gw0] PASSED tests/test_single_splunk_image.py::TestDockerSplunk::test_splunk_entrypoint_start_no_accept_license 
tests/test_single_splunk_image.py::TestDockerSplunk::test_splunk_entrypoint_no_provision 
[gw0] PASSED tests/test_single_splunk_image.py::TestDockerSplunk::test_splunk_entrypoint_no_provision 
tests/test_single_splunk_image.py::TestDockerSplunk::test_splunk_uid_gid 
[gw0] PASSED tests/test_single_splunk_image.py::TestDockerSplunk::test_splunk_uid_gid 
tests/test_single_splunk_image.py::TestDockerSplunk::test_compose_1so_trial
```

It'll hang on the test_compose_1so_trial, but your images will be created and ready to execute as per the offical instructions below.

```bash
$ docker run -p 8000:8000 -e "SPLUNK_PASSWORD=<password>" \
             -e "SPLUNK_START_ARGS=--accept-license" \
             -it --name so1 splunk-redhat-8
```

```bash
UID        PID  PPID  C STIME TTY          TIME CMD
ansible      1     0  0 21:21 ?        00:00:00 /bin/bash /sbin/entrypoint.sh start-service
ansible    204     0  0 21:21 pts/0    00:00:00 /bin/sh
splunk     971     1 13 21:21 ?        00:00:06 /rosetta/rosetta /opt/splunk/bin/splunkd -p 8089 start
splunk     972   971  0 21:21 ?        00:00:00 /rosetta/rosetta /opt/splunk/bin/splunkd -p 8089 start
splunk    1147   972  4 21:21 ?        00:00:01 mongod --dbpath=/opt/splunk/var/lib/splunk/kvstore/mongo --storageEngine=wiredTiger --wiredTigerCacheSizeGB=0.450000 --port=8191 --timeStampFormat=iso8601-utc --oplogSize=200 --keyFile=/opt/splunk/var/lib/spl
splunk    1301   972  2 21:21 ?        00:00:00 /rosetta/rosetta /opt/splunk/bin/splunkd instrument-resource-usage -p 8089 --with-kvstore
splunk    1334   972  2 21:21 ?        00:00:00 /rosetta/rosetta /opt/splunk/bin/python3.7 /opt/splunk/etc/apps/splunk_secure_gateway/bin/ssg_enable_modular_input.py
splunk    1351   972  3 21:21 ?        00:00:01 /rosetta/rosetta /opt/splunk/bin/python3.7 -O /opt/splunk/lib/python3.7/site-packages/splunk/appserver/mrsparkle/root.py --proxied=127.0.0.1,8065,8000
root      1885     1  0 21:21 ?        00:00:00 sudo -u splunk tail -n 0 -f /opt/splunk/var/log/splunk/splunkd_stderr.log
splunk    1886  1885  0 21:21 ?        00:00:00 /usr/bin/coreutils --coreutils-prog-shebang=tail /bin/tail -n 0 -f /opt/splunk/var/log/splunk/splunkd_stderr.log
splunk    1992   972  8 21:22 ?        00:00:00 /rosetta/rosetta /opt/splunk/bin/splunkd -p 8089 start
splunk    1993  1992  0 21:22 ?        00:00:00 /rosetta/rosetta /opt/splunk/bin/splunkd -p 8089 start
sh-4.4$ uname -a
Linux so1 5.15.49-linuxkit #1 SMP PREEMPT Tue Sep 13 07:51:32 UTC 2022 aarch64 aarch64 aarch64 GNU/Linux

```
Todo:

Redirect Aarch Python
Fix tests
Etc..etc

----

## Table of Contents

1. [Purpose](#purpose)
1. [Quickstart](#quickstart)
1. [Documentation](#documentation)
1. [Support](#support)
1. [Contributing](#contributing)
1. [License](#license)

----

## Purpose

#### What is Splunk Enterprise?
[Splunk Enterprise](https://www.splunk.com/en_us/software/splunk-enterprise.html) is a platform for operational intelligence. Our software lets you collect, analyze, and act upon the untapped value of big data that your technology infrastructure, security systems, and business applications generate. It gives you insights to drive operational performance and business results.

See [Splunk Products](https://www.splunk.com/en_us/software.html) for more information about the features and capabilities of Splunk products and how you can [bring them into your organization](https://www.splunk.com/en_us/enterprise-data-platform.html).

#### What is Docker-Splunk?
This is the official source code repository for building Docker images of Splunk Enterprise and Splunk Universal Forwarder. By introducing containerization, we can marry the ideals of infrastructure-as-code and declarative directives to manage and run Splunk Enterprise.

The provisioning of these containers is handled by the [Splunk-Ansible](https://github.com/splunk/splunk-ansible) project. Refer to the [Splunk-Ansible documentation](https://splunk.github.io/splunk-ansible/) and the [Ansible User Guide](https://docs.ansible.com/ansible/latest/user_guide/index.html) for more details.

----

## Quickstart

Start a single containerized instance of Splunk Enterprise with the command below, replacing `<password>` with a password string that conforms to the [Splunk Enterprise password requirements](https://docs.splunk.com/Documentation/Splunk/latest/Security/Configurepasswordsinspecfile).
```bash
$ docker run -p 8000:8000 -e "SPLUNK_PASSWORD=<password>" \
             -e "SPLUNK_START_ARGS=--accept-license" \
             -it --name so1 splunk-redhat-8:latest
```

This command does the following:
1. Starts a Docker container using the `splunk-redhat-8:latest` image that has been created by the makefile process
1. Names the container as `so1`.
1. Exposes a port mapping from the host's `8000` port to the container's `8000` port
1. Specifies a custom `SPLUNK_PASSWORD`.
1. Accepts the license agreement with `SPLUNK_START_ARGS=--accept-license`. This agreement must be explicitly accepted on every container or Splunk Enterprise doesn't start.

After the container starts up, you can access Splunk Web at <http://localhost:8000> with `admin:<password>`.

To view the logs from the container created above, run:
```bash
$ docker logs -f so1
```

To enter the container and run Splunk CLI commands, run:
```bash
# Defaults to the user "ansible"
docker exec -it so1 /bin/bash

# Run shell as the user "splunk"
docker exec -u splunk -it so1 bash
```

To enable TCP 10514 for listening, run:
```bash
docker exec -u splunk so1 /opt/splunk/bin/splunk add tcp 10514 \
    -sourcetype syslog -resolvehost true \
    -auth "admin:${SPLUNK_PASSWORD}"
```

To install an app, run:
```bash
docker exec -u splunk so1 /opt/splunk/bin/splunk install \
	/path/to/app.tar -auth "admin:${SPLUNK_PASSWORD}"

# Alternatively, apps can be installed at Docker run-time
docker run -e SPLUNK_APPS_URL=http://web/app.tgz ...
```

See [Deploy and run Splunk Enterprise inside a Docker container](https://docs.splunk.com/Documentation/Splunk/latest/Installation/DeployandrunSplunkEnterpriseinsideDockercontainers) for more information.

---

## Documentation
Visit the [Docker-Splunk documentation](https://splunk.github.io/docker-splunk/) page for full usage instructions, including installation, examples, and advanced deployment scenarios.

---

## Support
Use the [GitHub issue tracker](https://github.com/splunk/docker-splunk/issues) to submit bugs or request features.

If you have additional questions or need more support, you can:
* Post a question to [Splunk Answers](http://answers.splunk.com)
* Join the [#docker](https://splunk-usergroups.slack.com/messages/C1RH09ERM/) room in the [Splunk Slack channel](http://splunk-usergroups.slack.com). If you're a new Splunk customer you can register for Slack [here](http://splk.it/slack)
* If you are a Splunk Enterprise customer with a valid support entitlement contract and have a Splunk-related question, you can also open a support case on the https://www.splunk.com/ support portal

See the official [support guidelines](docs/SUPPORT.md) for more detailed information.

---

## Contributing
We welcome feedback and contributions from the community! See our [contribution guidelines](docs/CONTRIBUTING.md) for more information on how to get involved.

---

## License
Copyright 2018-2020 Splunk.

Distributed under the terms of our [license](docs/LICENSE.md), splunk-ansible is free and open source software.

## Authors
Splunk Inc. and the Splunk Community
# docker-splunk-silicon

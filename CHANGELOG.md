# Change Log

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a changelog](https://github.com/olivierlacan/keep-a-changelog).

## Unreleased

## [1.9.3](https://github.com/idealista/consul_role/tree/1.9.3) (2023-02-22)
### [Full Changelog](https://github.com/idealista/consul_role/compare/1.9.2...1.9.3)
### Fixed
- *[#91](https://github.com/idealista/consul_role/issues/91) install Python dependencies based on the Python interpreter being used* @ommarmol


## [1.9.2](https://github.com/idealista/consul_role/tree/1.9.2) (2022-09-29)
### [Full Changelog](https://github.com/idealista/consul_role/compare/1.9.1...1.9.2)
### Fixed
- *[#84](https://github.com/idealista/consul_role/issues/84) omit timeout if none is provided* @blalop


## [1.9.1](https://github.com/idealista/consul_role/tree/1.9.1) (2022-09-28)
### [Full Changelog](https://github.com/idealista/consul_role/compare/1.9.0...1.9.1)
### Fixed
- *[#84](https://github.com/idealista/consul_role/issues/84) service check timeout in healthcheck* @blalop


## [1.9.0](https://github.com/idealista/consul_role/tree/1.9.0) (2022-09-26)
### [Full Changelog](https://github.com/idealista/consul_role/compare/1.8.0...1.9.0)
### Added
- *[#84](https://github.com/idealista/consul_role/issues/84) Added service check timeout support* @blalop

## [1.8.0](https://github.com/idealista/consul_role/tree/1.8.0) (2021-12-23)
### [Full Changelog](https://github.com/idealista/consul_role/compare/1.7.1...1.8.0)
### Added
- *[#80](https://github.com/idealista/consul_role/issues/80) Added Debian11 support* @xtianae7
### Changed
- *Bumped dependencies* @xtianae7

## [1.7.1](https://github.com/idealista/consul_role/tree/1.7.1) (2021-02-25)
### [Full Changelog](https://github.com/idealista/consul_role/compare/1.7.0...1.7.1)
### Fixed
- *[#72](https://github.com/idealista/consul_role/issues/72) Fix logging for Debian 9 by using rsyslog* @caldito
### Deprecated
- The variable `private_tmp_service` is deprecated in favour of `consul_service_private_tmp`

## [1.7.0](https://github.com/idealista/consul_role/tree/1.7.0) (2021-02-23)
### [Full Changelog](https://github.com/idealista/consul_role/compare/1.6.0...1.7.0)
### Fixed
- *[#69](https://github.com/idealista/consul_role/issues/69) Fix logs, remove timestamp* @caldito
### Added
- *[#67](https://github.com/idealista/consul_role/pull/67) Allow to set grpc port* @vsuarez

## [1.6.0](https://github.com/idealista/consul_role/tree/1.6.0)
### [Full Changelog](https://github.com/idealista/consul_role/compare/1.5.0...1.6.0)
### Changed
- *[#64](https://github.com/idealista/consul_role/issues/64) Remove logrotate installation from role* @vsuarez

## [1.5.0](https://github.com/idealista/consul_role/tree/1.5.0)
### [Full Changelog](https://github.com/idealista/consul_role/compare/1.4.1...1.5.0)
### Added
- *[#58](https://github.com/idealista/consul_role/issues/58) *Add support for consul connect* @vicsufer
- *[#57](https://github.com/idealista/consul_role/issues/57) *Add LimitNOFILE configuration vars for consul.service* @blalop
- *[#60](https://github.com/idealista/consul_role/issues/60) *Add StandardOutput and StandardError configuration vars for consul.service* @blalop

## [1.4.1](https://github.com/idealista/consul_role/tree/1.4.1)
### [Full Changelog](https://github.com/idealista/consul_role/compare/1.4.0...1.4.1)
### Added
- *[#46](https://github.com/idealista/consul_role/issues/46) *Add private_tmp_service variable for consul.service* @xtianae7

## [1.4.0](https://github.com/idealista/consul_role/tree/1.4.0)
### [Full Changelog](https://github.com/idealista/consul_role/compare/1.3.0...1.4.0)
### Added
- *[#50](https://github.com/idealista/consul_role/issues/50) Add consul_service_sanity_healthcheck variable to enforce mandatory healthcheck on services* @vicsufer

## [1.3.0](https://github.com/idealista/consul_role/tree/1.3.0)
## [Full Changelog](https://github.com/idealista/consul_role/compare/1.2.5...1.3.0)
### Changed
- *[#46](https://github.com/idealista/consul_role/issues/46) Updated Ansible, molecule, goss; added buster testin; updated Travis config* @frantsao

## [1.2.5](https://github.com/idealista/consul_role/tree/1.2.5)
## [Full Changelog](https://github.com/idealista/consul_role/compare/1.2.4...1.2.5)
### Fixed
- *Upgraded default version to support log_file config option* @miguel-chacon
- *[#38](https://github.com/idealista/consul_role/issues/38) Register service error* @miguel-chacon

## [1.2.4](https://github.com/idealista/consul_role/tree/1.2.4)
## [Full Changelog](https://github.com/idealista/consul_role/compare/1.2.3...1.2.4)
### Fixed
- *[#30](https://github.com/idealista/consul_role/issues/30) Remove execution permission on service file* @miguel-chacon
- *[#8](https://github.com/idealista/consul_role/issues/8) Setup Travis CI* @miguel-chacon
- *Deregister agent before service stop* @miguel-chacon
### Changed
- *Support up to Consul v1.4 because of non ACLs retrocompability* [Consul Changelog](https://github.com/hashicorp/consul/blob/master/CHANGELOG.md#140-november-14-2018) @miguel-chacon
- *Update tests to Molecule 2* @miguel-chacon


## [1.2.3](https://github.com/idealista/consul_role/tree/1.2.3)
## [Full Changelog](https://github.com/idealista/consul_role/compare/1.2.2...1.2.3)
### Fixed
- *[#26](https://github.com/idealista/consul_role/issues/26) Fixing script health check* @dortegau

## [1.2.2](https://github.com/idealista/consul_role/tree/1.2.2)
## [Full Changelog](https://github.com/idealista/consul_role/compare/1.2.1...1.2.2)
### Fixed
- *[#23](https://github.com/idealista/consul_role/issues/23) Consul service restarting when changing version* @jnogol

## [1.2.1](https://github.com/idealista/consul_role/tree/1.2.1)
## [Full Changelog](https://github.com/idealista/consul_role/compare/1.2.0...1.2.1)
### Added
- *Ability to run the playbook with the `--check` flag* @michaelpporter

## [1.2.0](https://github.com/idealista/consul_role/tree/1.2.0)
## [Full Changelog](https://github.com/idealista/consul_role/compare/1.1.1...1.2.0)
### Added
- *Installation & version check* @jnogol

### Changed
- *Migrate tests to Goss* @jnogol

### Fixed
- *Servers can be set up without ACL* @jnogol

## [1.1.1](https://github.com/idealista/consul_role/tree/1.1.1)
## [Full Changelog](https://github.com/idealista/consul_role/compare/1.1.0...1.1.1)
### Fixed
- *[#13](https://github.com/idealista/consul_role/issues/13) Wrong Consul user home creation* @jnogol

## [1.1.0](https://github.com/idealista/consul_role/tree/1.1.0)
## [Full Changelog](https://github.com/idealista/consul_role/compare/1.0.1...1.1.0)
### Added
- *[#4](https://github.com/idealista/consul_role/issues/4) Services can be tagged during registration* @jnogol
- *[#5](https://github.com/idealista/consul_role/issues/5) Services can be now deregistered* @jnogol

### Changed
- *[#9](https://github.com/idealista/consul_role/issues/9) ACL files have now more restricted permissions. Tasks with token has no_log now* @jnogol
- *Update Consul version to 1.0.6* @jnogol

## [1.0.1](https://github.com/idealista/consul_role/tree/1.0.1)
## [Full Changelog](https://github.com/idealista/consul_role/compare/1.0.0...1.0.1)
### Fixed
- *[#1](https://github.com/idealista/consul_role/issues/1) python-consul needs openssl package* @jnogol

## [1.0.0](https://github.com/idealista/consul_role/tree/1.0.0)
- *First version*

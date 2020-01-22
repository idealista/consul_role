# Change Log

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a changelog](https://github.com/olivierlacan/keep-a-changelog).

## [Unreleased](https://github.com/idealista/consul-role/tree/develop)

## [1.2.5](https://github.com/idealista/consul-role/tree/1.2.5)
## [Full Changelog](https://github.com/idealista/consul-role/compare/1.2.4...1.2.5)
### Fixed
- *Upgraded default version to support log_file config option* @miguel-chacon
- *[#38](https://github.com/idealista/consul-role/issues/38) Register service error* @miguel-chacon

## [1.2.4](https://github.com/idealista/consul-role/tree/1.2.4)
## [Full Changelog](https://github.com/idealista/consul-role/compare/1.2.3...1.2.4)
### Fixed
- *[#30](https://github.com/idealista/consul-role/issues/30) Remove execution permission on service file* @miguel-chacon
- *[#8](https://github.com/idealista/consul-role/issues/8) Setup Travis CI* @miguel-chacon
- *Deregister agent before service stop* @miguel-chacon
### Changed
- *Support up to Consul v1.4 because of non ACLs retrocompability* [Consul Changelog](https://github.com/hashicorp/consul/blob/master/CHANGELOG.md#140-november-14-2018) @miguel-chacon
- *Update tests to Molecule 2* @miguel-chacon


## [1.2.3](https://github.com/idealista/consul-role/tree/1.2.3)
## [Full Changelog](https://github.com/idealista/consul-role/compare/1.2.2...1.2.3)
### Fixed
- *[#26](https://github.com/idealista/consul-role/issues/26) Fixing script health check* @dortegau

## [1.2.2](https://github.com/idealista/consul-role/tree/1.2.2)
## [Full Changelog](https://github.com/idealista/consul-role/compare/1.2.1...1.2.2)
### Fixed
- *[#23](https://github.com/idealista/consul-role/issues/23) Consul service restarting when changing version* @jnogol

## [1.2.1](https://github.com/idealista/consul-role/tree/1.2.1)
## [Full Changelog](https://github.com/idealista/consul-role/compare/1.2.0...1.2.1)
### Added
- *Ability to run the playbook with the `--check` flag* @michaelpporter

## [1.2.0](https://github.com/idealista/consul-role/tree/1.2.0)
## [Full Changelog](https://github.com/idealista/consul-role/compare/1.1.1...1.2.0)
### Added
- *Installation & version check* @jnogol

### Changed
- *Migrate tests to Goss* @jnogol

### Fixed
- *Servers can be set up without ACL* @jnogol

## [1.1.1](https://github.com/idealista/consul-role/tree/1.1.1)
## [Full Changelog](https://github.com/idealista/consul-role/compare/1.1.0...1.1.1)
### Fixed
- *[#13](https://github.com/idealista/consul-role/issues/13) Wrong Consul user home creation* @jnogol

## [1.1.0](https://github.com/idealista/consul-role/tree/1.1.0)
## [Full Changelog](https://github.com/idealista/consul-role/compare/1.0.1...1.1.0)
### Added
- *[#4](https://github.com/idealista/consul-role/issues/4) Services can be tagged during registration* @jnogol
- *[#5](https://github.com/idealista/consul-role/issues/5) Services can be now deregistered* @jnogol

### Changed
- *[#9](https://github.com/idealista/consul-role/issues/9) ACL files have now more restricted permissions. Tasks with token has no_log now* @jnogol
- *Update Consul version to 1.0.6* @jnogol

## [1.0.1](https://github.com/idealista/consul-role/tree/1.0.1)
## [Full Changelog](https://github.com/idealista/consul-role/compare/1.0.0...1.0.1)
### Fixed
- *[#1](https://github.com/idealista/consul-role/issues/1) python-consul needs openssl package* @jnogol

## [1.0.0](https://github.com/idealista/consul-role/tree/1.0.0)
- *First version*

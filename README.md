![Logo](https://raw.githubusercontent.com/idealista/consul_role/master/logo.gif)

# Consul Ansible role

Ansible role to install Consul (cluster of) server/client in a Debian environment.

- [Getting Started](#getting-started)
    - [Prerequisities](#prerequisities)
    - [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)

## Getting Started

These instructions will get you a copy of the role for your Ansible Playbook. Once launched, it will install Consul in a Debian system.

### Prerequisities

Ansible 4.x.x version installed.
Inventory destination should be a Debian environment.

Rsyslog needs should be installed. It can be done with this [role](https://github.com/idealista/rsyslog_role).

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Docker](https://www.docker.com/) as driver.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

``` yml
- src: idealista.consul_role
  version: 1.7.2
  name: consul
```

Install the role with ansible-galaxy command:

```
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

``` yml
---
- hosts: someserver
  roles:
    - consul
```

## Usage

Look to the defaults properties file (`defaults/main.yml`) to see the possible configuration properties.
Logging uses rsyslog by default. It can be changed by overriding the `consul_service_log_output` variable. It can be changed to `journal` or other options seen at the StandardOutput and StandardError sections in:
 * [Debian 9 systemd docs](https://manpages.debian.org/stretch/systemd/systemd.exec.5.en.html)
 * [Debian 10 and 11 systemd docs](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#StandardOutput=)
## Testing

```sh
$ pipenv sync
```

For more information read the [pipenv docs](https://docs.pipenv.org/).

### Testing

```sh
$ pipenv run molecule -c molecule/default/molecule.yml test 
```

## Built With

![Ansible](https://img.shields.io/badge/ansible-4.6.0-green.svg)
![Molecule](https://img.shields.io/badge/molecule-3.5.2-green.svg)
![Goss](https://img.shields.io/badge/goss-0.3.16-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/consul_role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/consul_role/contributors) who participated in this project.

## License

![Apache 2.0 License](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

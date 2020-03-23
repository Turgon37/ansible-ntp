Ansible Role NTP
=========

[![Build Status](https://travis-ci.com/Turgon37/ansible-ntp.svg?branch=master)](https://travis-ci.com/Turgon37/ansible-ntp)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-Turgon37.ntp-blue.svg)](https://galaxy.ansible.com/Turgon37/ntp/)

## Description

:grey_exclamation: Before using this role, please know that all my Ansible roles are fully written and accustomed to my IT infrastructure. So, even if they are as generic as possible they will not necessarily fill your needs, I advice you to carrefully analyse what they do and evaluate their capability to be installed securely on your servers.

This roles allow configuration of a NTP as a client or as a server.


## Requirements

Require Ansible >= 2.4

### Dependencies

## OS Family

This role is available for Debian and CentOS

## Features

This role can be used to :

  * install ntpd
  * configure it as client or server
  * monitoring items for
    * Zabbix
  * [local facts](#facts)

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below. To see default values please refer to this file.

| Name                                      | Types/Values   | Description                                                                             |
| ----------------------------------------- | ---------------|-----------------------------------------------------------------------------------------|
| `ntp__facts`                              | Boolean        | Install the local fact script                                                           |
| `ntp__monitoring`                         | String         | The name of the monitoring "profile" to use. Availables 'zabbix'                        |
| `ntp__service_enabled`                    | Boolean        | Enable of not the NTP daemon synchronisation of the host                                |
| `ntp__servers_default/global/group/host`  | List of string | Define additional NTP server on which to synchronize this host                          |
| `ntp__servers`                            | List of string | This variable bypass the defaults servers included in variables above                   |
| `ntp__listen_global/group/host`           | List of string | List of interfaces NTP should listen on                                                 |
| `ntp__peers`                              | List of string | List of ntp peers hosts                                                                 |
| `ntp__broadcast`                          | List of string | List of multicast or broadcast address to which diffuse time messages                   |
| `ntp__restrict_default/global/group/host` | List of rules  | The list of restricts rules (see below)                                                 |
| `ntp__facilities_global/group/host`       | Dict           | Define activation state off all facilities                                              |
| `ntp__fudge`                              | Boolean        | Enable fudge of the local time if server mode if desired and remote clock not available |
| `ntp__local_references`                   |                |                                                                                         |

### Restrict rules

Each restrict rule must define address, optional the netmask and the flags

```
ntp__restrict_group:
  - address: '10.1.1.0'
    mask: 255.255.255.0
    flags: kod notrap nomodify nopeer noquery
    order: 20
```

### Local references

You can configure this ntp server as a reference provider.
The type must be defined in ntp__local_reference_types and parameter depends on the selected type.
You have to check the official documentation to known about it.

```
ntp__local_references:
  # Fudge local clock if time servers is not available
  - type: 1
    parameters:
      stratum: 10
```


## Facts

By default the local fact are installed and expose the following variables :

```
ansible_local.ntp:
  version_full: '7.9p1'
  version_major: '7'
```

## Example

### Playbook

Use it in a playbook as follows:

```yaml
- hosts: all
  roles:
    - turgon37.ntp
```

### Inventory

To use this role create or update your playbook according the following example :

  * Simple NTP configured as client

```
ntp__servers: 'ntp.server.com'
```

  * NTP configured as server

```
ntp__servers: 'upper-stratum-server.example.com'
ntp__restrict_rules:
  '192.168.1.0/24': 'limited kod nomodify notrap nopeer'
```

  * NTP configured as server with broadcast enabled

```
ntp__servers: 'upper-stratum-server.example.com'
ntp__restrict_rules:
  '192.168.1.0/24': 'limited kod nomodify notrap nopeer'
ntp__broadcast:
  - '192.168.1.255'
```

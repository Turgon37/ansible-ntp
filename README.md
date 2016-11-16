Ansible Role NTP
========

This roles allow configuration of a ntp daemon on a host

## OS Family

This role is available for Debian and CentOS

## Features

At this day the role can be used to configure :

  * NTP client
  * NTP server

## Configuration

The variables that can be passed to this role and a brief description about them are as follows:

| Name                  | Description                                                                              |
| --------------------- | ---------------------------------------------------------------------------------------- |
| ntp__daemon_enabled   |  Enable of not the NTP daemon synchronisation of the host                                |
| ntp__daemon           |  The name of the daemon type to use. Available choice in ['ntpd']                        |
| ntp__conflict_packages|  The list of others conflict packages to remove according to the selected daemon type    |
| ntp__servers_map      |  The map that contains the ntp server for each distribution                              |
| ntp__fudge            |  Enable fudge of the local time if server mode if desired and remote clock not available |
| ntp__localclock       |  Provide local clock as reference by default                                             |
| ntp__broadcast        |  The list of broadcast address(es) to whose send time                                    |
| ntp__restrict_rules   |  The list of restricts rules (see below)                                                 |

### Example

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
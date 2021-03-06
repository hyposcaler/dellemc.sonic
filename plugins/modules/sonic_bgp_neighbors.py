#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for sonic_bgp_neighbors
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = """
---
module: sonic_bgp_neighbors
version_added: 1.0.0
short_description: Configures BGP neighbors on Enterprise SONiC.
description:
  - This module provides configuration management of BGP neighbor parameters for devices runnin
    Enterprise SONiC Distribution by Dell Technologies.
  - bgp_as and vrf_name need be created earlier in the device.
author: "Abirami N (@abirami-n)"

options:
  config:
    description: Specifies the BGP neighbors related configuration.
    type: list
    elements: dict
    suboptions:
      bgp_as:
        description:
          - Specifies the BGP autonomous system (AS) number which is already configured in the device.
        type: str
        required: True
      vrf_name:
        description:
          - Specifies the VRF name which is already configured in the device.
        default: default
        type: str
      peer_group:
        description: Specifies the list of peer groups.
        type: list
        elements: dict
        suboptions:
          name:
            description: Name of the peer group.
            type: str
            required: True
          remote_as:
            description:
              - Remote AS of the BGP peer group to configure.
              - peer_as and peer_type are mutually exclusive.
            type: dict
            suboptions:
              peer_as:
                description:
                  - Specifies remote AS number.
                  - Range is from 1 to 4294967295.
                type: int
              peer_type:
                description:
                  - Specifies type of BGP peer.
                type: str
                choices:
                  - internal
                  - external
          bfd:
            description:
              - Enables or disabls BFD.
            type: bool
          advertisement_interval:
            description:
              - Specifies the minimum interval between sending BGP routing updates
              - Range is from 0 to 600.
            type: int
          timers:
            description:
              - Specifies BGP peer group timer related configurations.
            type: dict
            suboptions:
              keepalive:
                description:
                  - Frequency (in seconds) with which the device sends keepalive messages to its peer.
                  - Range is from 0 to 65535.
                type: int
              holdtime:
                description:
                  - Interval (in seconds) after not receiving a keepalive message that SONiC declares a peer dead.
                  - Range is from 0 to 65535.
                type: int
          capability:
            description:
              - Specifies capability attributes to this peer group.
            type: dict
            suboptions:
              dynamic:
                description:
                  - Enables or disables dynamic capability to this peer group.
                type: bool
              extended_nexthop:
                description:
                  - Enables or disables advertise extended next-hop capability to the peer.
                type: bool
      neighbors:
        description: Specifies BGP neighbor related configurations.
        type: list
        elements: dict
        suboptions:
          neighbor:
            description:
              - Neighbor router address.
            type: str
            required: True
          remote_as:
            description:
              - Remote AS of the BGP neighbor to configure.
              - peer_as and peer_type are mutually exclusive.
            type: dict
            suboptions:
              peer_as:
                description:
                  - Specifies remote AS number.
                  - Range is from 1 to 4294967295.
                type: int
              peer_type:
                description:
                  - Specifies type of BGP peer.
                type: str
                choices:
                  - internal
                  - external
          bfd:
            description:
              - Enables or disables BFD.
            type: bool
          advertisement_interval:
            description:
              - Specifies the minimum interval between sending BGP routing updates
              - Range is from 0 to 600.
            type: int
          peer_group:
            description:
              - Name of the peer group that the neighbor is a member of.
            type: str
          timers:
            description:
              - Specifies BGP neighbor timer-related configurations.
            type: dict
            suboptions:
              keepalive:
                description:
                  - Frequency (in seconds) with which the device sends keepalive messages to its peer.
                  - Range is from 0 to 65535.
                type: int
              holdtime:
                description:
                  - Interval (in seconds) after not receiving a keepalive message that SONiC declares a peer dead.
                  - Range is from 0 to 65535.
                type: int
          capability:
            description:
              - Specifies capability attributes to this neighbor.
            type: dict
            suboptions:
              dynamic:
                description:
                  - Enables or disables dynamic capability to this neighbor
                type: bool
              extended_nexthop:
                description:
                  - Enables or disables advertise extended next-hop capability to the peer.
                type: bool

  state:
    description:
      - Specifies the operation to be performed on the BGP process configured on the device.
      - In case of merged, the input configuration will be merged with the existing BGP configuration on the device.
      - In case of deleted, the existing BGP configuration will be removed from the device.
    default: merged
    type: str
    choices:
      - merged
      - deleted
"""
EXAMPLES = """
# Using deleted
#
# Before state:
# -------------
#router bgp 11 vrf VrfCheck2
# network import-check
# timers 60 180
#!
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
# !
# neighbor interface Ethernet12
#!
#router bgp 11
# network import-check
# timers 60 180
# !
# neighbor 192.168.1.4
# !
# peer-group SP1
#  bfd
#  capability dynamic
# !
# peer-group SP2
# !
#
#- name: Deletes all BGP neighbors.
#  sonic_bgp_neighbors:
#    config:
#    state: deleted
#
#
# After state:
# -------------
#router bgp 11 vrf VrfCheck2
# network import-check
# timers 60 180
#!
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
#!
#router bgp 11
# network import-check
# timers 60 180
# !
#
# Using merged
#
# Before state:
# ------------
#router bgp 11 vrf VrfCheck2
# network import-check
# timers 60 180
#!
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
#!
#router bgp 11
# network import-check
# timers 60 180
# !
#
#- name: "Adds sonic_bgp_neighbors"
#  sonic_bgp_neighbors:
#    config:
#      - bgp_as: 51
#        vrf_name: VrfReg1
#        peer_group:
#          - name: SPINE
#            bfd: true
#            capability:
#              dynamic: true
#              extended_nexthop: true
#            remote_as:
#              peer_as: 4
#        neighbors:
#          - neighbor: Ethernet12
#            remote_as:
#              peer_as: 10
#            peer_group: SPINE
#            advertisement_interval: 15
#            timers:
#              keepalive: 30
#              holdtime: 15
#            bfd: true
#            capability:
#              dynamic: true
#              extended_nexthop: true
#          - neighbor: 192.168.1.4
#    state: merged
#
# After state:
# ------------
#!
#router bgp 11 vrf VrfCheck2
# network import-check
# timers 60 180
#!
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
# !
# peer-group SPINE
#  remote-as 4
#  bfd
#  capability dynamic
#  capability extended-nexthop
# !
# neighbor interface Ethernet12
#  peer-group SPINE
#  remote-as 10
#  timers 15 30
#  advertisement-interval 15
#  bfd
#  capability extended-nexthop
#  capability dynamic
# !
# neighbor 192.168.1.4
#!
#router bgp 11
# network import-check
# timers 60 180
#
# Using deleted
#
# Before state:
# ------------
#!
#router bgp 11 vrf VrfCheck2
# network import-check
# timers 60 180
#!
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
# !
# peer-group SPINE
#  bfd
#  remote-as 4
# !
# neighbor interface Ethernet12
#  peer-group SPINE
#  remote-as 10
#  timers 15 30
#  advertisement-interval 15
#  bfd
#  capability extended-nexthop
#  capability dynamic
# !
# neighbor 192.168.1.4
#!
#router bgp 11
# network import-check
# timers 60 18
# !
# peer-group SP
# !
# neighbor interface Ethernet8
#
#- name: "Deletes sonic_bgp_neighbors and peer-groups specific to vrfname"
#  sonic_bgp_neighbors:
#    config:
#      - bgp_as: 51
#        vrf_name: VrfReg1
#    state: deleted
#
# After state:
# ------------
#!
#router bgp 11 vrf VrfCheck2
# network import-check
# timers 60 180
#!
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
# !
#router bgp 11
# network import-check
# timers 60 18
# !
# peer-group SP
# !
# neighbor interface Ethernet8
#
# Using deleted
#
# Before state:
# -------------
#
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
# !
# peer-group SPINE
#  bfd
#  remote-as 4
# !
# neighbor interface Ethernet12
#  peer-group SPINE
#  remote-as 10
#  timers 15 30
#  advertisement-interval 15
#  bfd
#  capability extended-nexthop
#  capability dynamic
# !
# neighbor 192.168.1.4
# !
#- name: "Deletes specific sonic_bgp_neighbors"
#  sonic_bgp_neighbors:
#    config:
#      - bgp_as: 51
#        vrf_name: VrfReg1
#        peer_group:
#          - name: SPINE
#            bfd: true
#            remote_as:
#              peer_as: 4
#        neighbors:
#          - neighbor: Ethernet12
#            remote_as:
#              peer_as: 10
#            peer_group: SPINE
#            advertisement_interval: 15
#            timers:
#              keepalive: 30
#              holdtime: 15
#            bfd: true
#            capability:
#              dynamic: true
#              extended_nexthop: true
#          - neighbor: 192.168.1.4
#    state: deleted
#
# After state:
# -------------
#
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
# !
# peer-group SPINE
# !
# neighbor interface Ethernet12
# !

"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.argspec.bgp_neighbors.bgp_neighbors import Bgp_neighborsArgs
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.config.bgp_neighbors.bgp_neighbors import Bgp_neighbors


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Bgp_neighborsArgs.argument_spec,
                           supports_check_mode=True)

    result = Bgp_neighbors(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()

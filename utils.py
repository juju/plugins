#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import yaml


class ServiceUnit(object):
    def __init__(self, name, unit_data, subordinate=False):
        self.name = name
        self.subordinate = subordinate
        self._data = {'public-address': '', 'open-ports': [],
                      'agent-state': '',
                      'subordinates': None}
        self._data.update(unit_data)

    def __getattr__(self, item):
        return self._data[item.replace('_', '-')]

    def __getitem__(self, item):
        return self._data[item]


def juju_get(service, juju_env=None):
    cmd = ['juju', 'get', service]
    if juju_env:
        cmd.append(['-e', juju_env])
    status_raw = subprocess.check_output(cmd)
    return yaml.safe_load(status_raw)


def get_juju_status(juju_env=None):
    cmd = ['juju', 'status']
    if juju_env:
        cmd.append(['-e', juju_env])
    status_raw = subprocess.check_output(cmd)
    return yaml.safe_load(status_raw)


def get_units(subordinates=True):
    status = get_juju_status()

    units = []
    for service in status['services']:
        if 'units' in status['services'][service]:
            for u in status['services'][service]['units']:
                unit = ServiceUnit(u, status['services'][service]['units'][u])
                units.append(unit)
                if subordinates and unit.subordinates:
                    for s in unit.subordinates:
                        units.append(ServiceUnit(s, unit.subordinates[s],
                                                 subordinate=True))
    return units


def print_unit(unit, indent=0, quiet=False):
    status_line = "%s: %s %s (%s)"
    if not quiet:
        status_line = "%s- " + status_line
    else:
        indent = 0
        status_line = "%s" + status_line

    print status_line % (" " * indent, unit.name,
                         unit['public-address'],
                         ', '.join(unit['open-ports']), unit['agent-state'])

# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Felix Fontein
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class ModuleDocFragment(object):

    # Standard files documentation fragment
    DOCUMENTATION = r'''
options:
    hetzner_token:
        description:
          - The token for the Hetzner API.
          - If not provided, will be read from the environment variable C(HETZNER_DNS_TOKEN).
        aliases:
          - api_token
        type: str
        required: true
'''

    PLUGIN = r'''
options:
    hetzner_token:
        env:
          - name: HETZNER_DNS_TOKEN
'''

    ZONE_ID_TYPE = r'''
options:
    zone_id:
        type: str
'''

    ZONE_CHOICES = r'''
options:
    type:
        choices: ['A', 'AAAA', 'NS', 'MX', 'CNAME', 'RP', 'TXT', 'SOA', 'HINFO', 'SRV', 'DANE', 'TLSA', 'DS', 'CAA']
'''

    ZONE_CHOICES_RECORD_SETS_MODULE = r'''
options:
    record_sets:
        suboptions:
            type:
                choices: ['A', 'AAAA', 'NS', 'MX', 'CNAME', 'RP', 'TXT', 'SOA', 'HINFO', 'SRV', 'DANE', 'TLSA', 'DS', 'CAA']
        # The following madness is needed because of the primitive merging of docs fragments:
        # (It must be kept in sync with the equivalent lines in module_record_sets.py!)
                description:
                  - The type of DNS record to create or delete.
                required: true
                type: str
            record:
                description:
                  - The full DNS record to create or delete.
                  - Exactly one of I(record) and I(prefix) must be specified.
                type: str
            prefix:
                description:
                  - The prefix of the DNS record.
                  - This is the part of I(record) before I(zone). For example, if the record to be modified is C(www.example.com)
                    for the zone C(example.com), the prefix is C(www). If the record in this example would be C(example.com), the
                    prefix would be C('') (empty string).
                  - Exactly one of I(record) and I(prefix) must be specified.
                type: str
            ttl:
                description:
                  - The TTL to give the new record, in seconds.
                default: 3600
                type: int
            value:
                description:
                  - The new value when creating a DNS record.
                  - YAML lists or multiple comma-spaced values are allowed.
                  - When deleting a record all values for the record must be specified or it will
                    not be deleted.
                  - Must be specified if I(ignore=false).
                type: list
                elements: str
            ignore:
                description:
                  - If set to C(true), I(value) will be ignored.
                  - This is useful when I(prune=true), but you do not want certain entries to be removed
                    without having to know their current value.
                type: bool
                default: false
'''

    ZONE_CHOICES_RECORDS_INVENTORY = r'''
options:
    filters:
        suboptions:
            type:
                choices: ['A', 'AAAA', 'NS', 'MX', 'CNAME', 'RP', 'TXT', 'SOA', 'HINFO', 'SRV', 'DANE', 'TLSA', 'DS', 'CAA']
        # The following madness is needed because of the primitive merging of docs fragments:
        # (It must be kept in sync with the equivalent lines in inventory_records.py!)
                description:
                  - Record types whose values to use.
                type: list
                elements: string
                default: [A, AAAA, CNAME]
'''
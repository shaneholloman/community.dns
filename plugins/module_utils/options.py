# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Felix Fontein
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


from ansible_collections.community.dns.plugins.module_utils.argspec import (
    ArgumentSpec,
)


def create_bulk_operations_argspec(provider_information):
    """
    If the provider supports bulk operations, return an ArgumentSpec object with appropriate
    options. Otherwise return an empty one.
    """
    if not provider_information.supports_bulk_actions():
        return ArgumentSpec()

    return ArgumentSpec(
        argument_spec=dict(
            bulk_operation_threshold=dict(type='int', default=2),
        ),
    )
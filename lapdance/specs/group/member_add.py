# -*- coding: utf-8 -*-

from lapdance.specs.group import ldap_operation_spec
from lapdance.specs.group import tags, group_id_path
from lapdance.specs.constants import GROUP_MEMBER_ADD
from copy import deepcopy

group_member_add = deepcopy(ldap_operation_spec)
group_member_add['tags'] = tags
group_member_add['summary'] = GROUP_MEMBER_ADD

group_member_add['parameters'] = [
    group_id_path,
    {
        'type': 'object',
        'name': 'body',
        'required': True,
        'in': 'body',
        'schema': {
            'required': ['id'],
            'properties': {
                'id': {
                    'type': 'string',
                    'description': 'User id',
                    'example': 'monty.python'
                },
                'fix': {
                    'type': 'string',
                    'default': False,
                    'description': 'Add even if already relationship already exists'
                }
            }
        }
    },
]

group_member_add['description'] = 'Adds user to group',
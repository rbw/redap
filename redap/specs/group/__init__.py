# -*- coding: utf-8 -*-

from functools import partial

from redap.settings import REDAP_LDAP_GROUP
from redap.utils import generate_spec_def
from redap.specs.definitions import (
    op_success, op_success_def,
    op_ldap_error, op_ldap_error_def,
    op_error, op_error_def
)

tags = ['groups']
group_id_path = {
    'name': 'group_id',
    'in': 'path',
    'type': 'string',
    'required': 'true',
}

group_body = {
    'type': 'object',
    'name': 'body',
    'required': True,
    'in': 'body',
    'schema': {
        '$ref': '#/definitions/Group'
    },
}

get_group_def = partial(generate_spec_def, 'Group', REDAP_LDAP_GROUP)


ldap_operation_spec = {
    'tags': tags,
    'summary': '<Unknown>',
    'parameters': [group_id_path],
    'definitions': {
        **get_group_def(),
        **op_success_def,
        **op_ldap_error_def,
        **op_error_def,
    },
    'responses': {
        '201': op_success,
        '400': op_error,
        '500': op_ldap_error,
    }
}

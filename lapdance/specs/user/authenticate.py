# -*- coding: utf-8 -*-

from lapdance.specs.user import tags
from lapdance.specs.definitions import (
    op_success, op_success_def,
    op_ldap_error, op_ldap_error_def,
    op_error, op_error_def
)
from lapdance.specs.descriptions import USER_AUTHENTICATE

user_authenticate = {
    'tags': tags,
    'summary': USER_AUTHENTICATE,
    'parameters': [{
        'type': 'object',
        'name': 'body',
        'required': True,
        'in': 'body',
        'schema': {
            '$ref': '#/definitions/Credentials'
        },
    }],
    'definitions': {
        'Credentials': {
            'type': 'object',
            'required': ['username', 'password'],
            'properties': {
                'username': {
                    'type': 'string'
                },
                'password': {
                    'type': 'string'
                }
            }
        },
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

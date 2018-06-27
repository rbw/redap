# -*- coding: utf-8 -*-

from redap.specs.user import get_user_def, user_id_path, tags
from redap.specs.definitions import (
    op_success, op_success_def,
    op_ldap_error, op_ldap_error_def,
    op_error, op_error_def
)
from redap.specs.descriptions import USER_PASSWORD

user_password = {
    'tags': tags,
    'summary': USER_PASSWORD,
    'parameters': [
        user_id_path,
        {
            'type': 'object',
            'name': 'body',
            'required': True,
            'in': 'body',
            'schema': {
                '$ref': '#/definitions/PasswordChange'
            }
        }
    ],
    'definitions': {
        'PasswordChange': {
            'type': 'object',
            'required': ['new_password'],
            'properties': {
                'new_password': {
                    'type': 'string'
                },
                'old_password': {
                    'type': 'string'
                }
            }
        },
        **get_user_def(),
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

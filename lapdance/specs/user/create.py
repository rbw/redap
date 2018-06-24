# -*- coding: utf-8 -*-

from lapdance.specs.user import get_user_def, user_body, tags
from lapdance.specs.definitions import (
    op_success, op_success_def,
    op_ldap_error, op_ldap_error_def,
    op_error, op_error_def
)
from lapdance.specs.descriptions import USER_CREATE

user_create = {
    'tags': tags,
    'summary': USER_CREATE,
    'parameters': [user_body],
    'definitions': {
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

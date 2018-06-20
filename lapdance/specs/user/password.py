# -*- coding: utf-8 -*-

from lapdance.specs.user import get_user_def, user_id_path, tags
from lapdance.specs.common import (
    op_success, op_success_def,
    op_ldap_error, op_ldap_error_def,
    op_error, op_error_def
)
from lapdance.specs.constants import USER_PASSWORD

user_password = {
    'tags': tags,
    'summary': USER_PASSWORD,
    'parameters': [user_id_path],
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

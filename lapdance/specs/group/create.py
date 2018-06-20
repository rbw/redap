# -*- coding: utf-8 -*-

from lapdance.specs.group import get_group_def, group_body, tags
from lapdance.specs.common import (
    op_success, op_success_def,
    op_ldap_error, op_ldap_error_def,
    op_error, op_error_def
)
from lapdance.specs.constants import GROUP_CREATE

group_create = {
    'tags': tags,
    'summary': GROUP_CREATE,
    'parameters': [group_body],
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

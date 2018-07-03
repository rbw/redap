# -*- coding: utf-8 -*-

from redap.specs.definitions import LDAP_OPERATION
from redap.specs.utils import get_body_param
from . import get_user_spec, param_path

credentials = {
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
    }
}

data = get_user_spec(
    summary='Set new password',
    params=[param_path, get_body_param('PasswordChange')],
    defs=[credentials],
    responses=[(201, LDAP_OPERATION)]
)

# -*- coding: utf-8 -*-

from redap.specs.definitions import LDAP_OPERATION
from redap.specs.utils import get_body_param
from . import get_user_spec, param_path

credentials = {
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
    }
}

data = get_user_spec(
    summary='Authenticate user',
    params=[get_body_param('Credentials')],
    defs=[credentials],
    responses=[(201, LDAP_OPERATION)]
)

# -*- coding: utf-8 -*-

from redap.specs.definitions import LDAP_OPERATION
from redap.specs.utils import get_body_param
from . import get_group_spec, param_path

MemberAdd = {
    'MemberAdd': {
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
                'description': 'Overwrite existing relationship'
            }
        }
    }
}

data = get_group_spec(
    summary='Add user to group',
    params=[param_path, get_body_param('MemberAdd')],
    defs=[MemberAdd],
    responses=[(201, LDAP_OPERATION)]
)

# -*- coding: utf-8 -*-

from redap.specs.common import filter_param, nested_param
from redap.specs.user import def_users
from . import get_group_spec

response_def = {
    'definition': def_users,
    'response': {
        'description': 'List of members',
        'schema': {
            '$ref': '#/definitions/User'
        }
    }
}

data = get_group_spec(
    summary='Get list of members',
    params=[
        filter_param,
        nested_param
    ],
    responses=[(200, response_def)]
)

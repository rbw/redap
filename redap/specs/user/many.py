# -*- coding: utf-8 -*-

from redap.specs.common import filter_param
from . import get_user_spec, def_user

response_def = {
    'definition': def_user,
    'response': {
        'description': 'List of users',
        'schema': {
            '$ref': '#/definitions/User'
        }
    }
}

data = get_user_spec(
    summary='Get list of users',
    params=[filter_param],
    responses=[(200, response_def)]
)

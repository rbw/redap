# -*- coding: utf-8 -*-

from redap.specs.common import filter_param, nested_param
from redap.specs.group import def_groups
from . import get_user_spec, param_path

response_def = {
    'definition': def_groups,
    'response': {
        'description': 'List of groups',
        'schema': {
            '$ref': '#/definitions/Group'
        }
    }
}

data = get_user_spec(
    summary='List group memberships',
    params=[
        param_path,
        filter_param,
        nested_param
    ],
    responses=[(200, response_def)]
)

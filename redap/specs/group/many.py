# -*- coding: utf-8 -*-

from redap.specs.common import filter_param
from . import get_group_spec, def_group

response_def = {
    'definition': def_group,
    'response': {
        'description': 'List of groups',
        'schema': {
            '$ref': '#/definitions/Group'
        }
    }
}

data = get_group_spec(
    summary='Get list of groups',
    params=[filter_param],
    responses=[(200, response_def)]
)

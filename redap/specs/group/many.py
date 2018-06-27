# -*- coding: utf-8 -*-

from redap.specs.group import tags
from redap.specs.definitions import (
    op_error, op_error_def, many_filter_param
)
from redap.specs.descriptions import GROUP_MANY

group_many = {
    'tags': tags,
    'summary': GROUP_MANY,
    'parameters': [many_filter_param],
    'definitions': {
        **op_error_def,
        'Groups': {
            'type': 'array',
            'items': {
                '$ref': '#/definitions/Group'
            }
        },
    },
    'responses': {
        '200': {
            'description': 'List of groups',
            'schema': {
                '$ref': '#/definitions/Groups'
            },
        },
        '400': op_error,
    }
}

# -*- coding: utf-8 -*-

from redap.specs.user import tags
from redap.specs.descriptions import USER_MANY
from redap.specs.definitions import (
    op_error, op_error_def, many_filter_param
)

user_many = {
    'tags': tags,
    'summary': USER_MANY,
    'parameters': [many_filter_param],
    'definitions': {
        **op_error_def,
        'Users': {
            'type': 'array',
            'items': {
                '$ref': '#/definitions/User'
            }
        },
    },
    'responses': {
        '200': {
            'schema': {
                '$ref': '#/definitions/Users'
            },
        },
        '400': op_error,
    }
}

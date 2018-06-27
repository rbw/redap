# -*- coding: utf-8 -*-

from redap.specs.user import get_user_def, tags, user_id_path
from redap.specs.definitions import (
    op_error, op_error_def
)
from redap.specs.descriptions import USER_ONE

user_one = {
    'tags': tags,
    'summary': USER_ONE,
    'parameters': [user_id_path],
    'definitions': {
        **get_user_def(),
        **op_error_def,
    },
    'responses': {
        '200': {
            'schema': {
                '$ref': '#/definitions/User'
            },
        },
        '400': op_error,
    }
}

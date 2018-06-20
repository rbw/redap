# -*- coding: utf-8 -*-

from lapdance.specs.user import get_user_def, tags, user_id_path
from lapdance.specs.common import (
    op_error, op_error_def
)
from lapdance.specs.constants import USER_ONE

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

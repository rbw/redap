# -*- coding: utf-8 -*-

from lapdance.specs.user import tags, user_id_path, user_body, get_user_def
from lapdance.specs.definitions import (
    op_success, op_success_def,
    op_error, op_error_def
)
from lapdance.specs.descriptions import USER_UPDATE


user_update = {
    'tags': tags,
    'summary': USER_UPDATE,
    'parameters': [
        user_id_path,
        user_body,
    ],
    'definitions': {
        **get_user_def(),
        **op_success_def,
        **op_error_def,
    },
    'responses': {
        '200': op_success,
        '400': op_error,
    }
}

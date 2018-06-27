# -*- coding: utf-8 -*-

from redap.specs.group import get_group_def, tags, group_id_path, group_body
from redap.specs.definitions import (
    op_success, op_success_def,
    op_error, op_error_def
)
from redap.specs.descriptions import GROUP_UPDATE

group_update = {
    'tags': tags,
    'summary': GROUP_UPDATE,
    'parameters': [
        group_id_path,
        group_body,
    ],
    'definitions': {
        **get_group_def(),
        **op_success_def,
        **op_error_def,
    },
    'responses': {
        '200': op_success,
        '400': op_error,
    }
}

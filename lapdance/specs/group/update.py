# -*- coding: utf-8 -*-

from lapdance.specs.group import get_group_def, tags, group_id_path, group_body
from lapdance.specs.common import (
    op_success, op_success_def,
    op_error, op_error_def
)
from lapdance.specs.constants import GROUP_UPDATE

group_update = {
    'tags': tags,
    'summary': GROUP_UPDATE,
    'parameters': [
        group_id_path,
        group_body,
    ],
    'definitions': {
        **get_group_def(required_fields=[]),
        **op_success_def,
        **op_error_def,
    },
    'responses': {
        '200': op_success,
        '400': op_error,
    }
}

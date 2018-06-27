# -*- coding: utf-8 -*-

from redap.specs.group import get_group_def, tags, group_id_path
from redap.specs.definitions import (
    op_error, op_error_def
)
from redap.specs.descriptions import GROUP_ONE

group_one = {
    'tags': tags,
    'summary': GROUP_ONE,
    'parameters': [group_id_path],
    'definitions': {
        **get_group_def(),
        **op_error_def,
    },
    'responses': {
        '200': {
            'schema': {
                '$ref': '#/definitions/Group'
            },
        },
        '400': op_error,
    }
}

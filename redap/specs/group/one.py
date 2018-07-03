# -*- coding: utf-8 -*-

from . import get_group_spec, def_group, param_path

response_def = {
    'definition': def_group,
    'response': {
        "description": "Single group",
        "schema": {
            "$ref": "#/definitions/Group"
        }
    }
}

data = get_group_spec(
    summary='Get single group',
    params=[param_path],
    responses=[(200, response_def)]
)

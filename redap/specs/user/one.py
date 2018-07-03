# -*- coding: utf-8 -*-

from . import get_user_spec, def_user, param_path

response_def = {
    'definition': def_user,
    'response': {
        "description": "Single user",
        "schema": {
            "$ref": "#/definitions/User"
        }
    }
}

data = get_user_spec(
    summary='Get single user',
    params=[param_path],
    responses=[(200, response_def)]
)

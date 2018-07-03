# -*- coding: utf-8 -*-

from functools import partial
from redap.settings import user_schema
from redap.specs import get_spec
from redap.specs.utils import get_path_param, get_body_param, def_from_schema

def_name = 'User'

tags = [def_name]
param_path = get_path_param('user_id')
param_body = get_body_param(def_name)

def_user = def_from_schema(def_name, user_schema.data)
def_users = def_from_schema(def_name, user_schema.data, many=True)
get_user_spec = partial(get_spec, tag=def_name)

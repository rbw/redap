# -*- coding: utf-8 -*-

from functools import partial
from redap.settings import group_schema
from redap.specs import get_spec
from redap.specs.utils import get_path_param, get_body_param, def_from_schema

def_name = 'Group'

tags = [def_name]
param_path = get_path_param('group_id')
param_body = get_body_param(def_name)

def_group = def_from_schema(def_name, group_schema.data)
def_groups = def_from_schema(def_name, group_schema.data, many=True)
get_group_spec = partial(get_spec, tag=def_name)

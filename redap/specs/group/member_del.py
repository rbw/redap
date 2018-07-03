# -*- coding: utf-8 -*-

from redap.specs.definitions import LDAP_OPERATION
from redap.specs.user import param_path as user_param_path
from . import param_path as group_param_path, get_group_spec

data = get_group_spec(
    summary='Remove user from group',
    params=[group_param_path, user_param_path],
    responses=[(201, LDAP_OPERATION)]
)

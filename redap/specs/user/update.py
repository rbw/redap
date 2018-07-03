# -*- coding: utf-8 -*-

from redap.specs.definitions import LDAP_OPERATION
from . import param_body, param_path, get_user_spec, def_user

data = get_user_spec(
    summary='Update user',
    params=[param_path, param_body],
    defs=[def_user],
    responses=[(201, LDAP_OPERATION)]
)

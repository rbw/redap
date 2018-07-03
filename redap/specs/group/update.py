# -*- coding: utf-8 -*-

from redap.specs.definitions import LDAP_OPERATION
from . import param_body, param_path, get_group_spec, def_group

data = get_group_spec(
    summary='Update group',
    params=[param_path, param_body],
    defs=[def_group],
    responses=[(201, LDAP_OPERATION)]
)

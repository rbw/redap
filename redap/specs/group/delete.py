# -*- coding: utf-8 -*-

from redap.specs.definitions import LDAP_OPERATION
from . import param_path, get_group_spec, def_group

data = get_group_spec(
    summary='Remove group',
    params=[param_path],
    defs=[def_group],
    responses=[(200, LDAP_OPERATION)]
)

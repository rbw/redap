# -*- coding: utf-8 -*-

from redap.specs.definitions import LDAP_OPERATION
from . import param_path, get_user_spec, def_user

data = get_user_spec(
    summary='Remove user',
    params=[param_path],
    defs=[def_user],
    responses=[(200, LDAP_OPERATION)]
)

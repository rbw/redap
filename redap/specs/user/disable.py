# -*- coding: utf-8 -*-

from redap.specs.definitions import LDAP_OPERATION
from . import param_path, get_user_spec

data = get_user_spec(
    summary='Disable user',
    params=[param_path],
    responses=[(201, LDAP_OPERATION)]
)

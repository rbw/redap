# -*- coding: utf-8 -*-

from lapdance.specs.user import ldap_operation_spec
from lapdance.specs.descriptions import USER_ENABLE
from copy import deepcopy

user_enable = deepcopy(ldap_operation_spec)
user_enable['summary'] = USER_ENABLE

# -*- coding: utf-8 -*-

from lapdance.specs.user import ldap_operation_spec
from lapdance.specs.constants import USER_UNLOCK
from copy import deepcopy

user_unlock = deepcopy(ldap_operation_spec)
user_unlock['summary'] = USER_UNLOCK

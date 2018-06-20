# -*- coding: utf-8 -*-

from lapdance.specs.user import ldap_operation_spec
from lapdance.specs.constants import USER_PW_NEVER_EXPIRES
from copy import deepcopy

user_pw_never_expires = deepcopy(ldap_operation_spec)
user_pw_never_expires['summary'] = USER_PW_NEVER_EXPIRES

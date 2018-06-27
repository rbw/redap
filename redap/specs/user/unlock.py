# -*- coding: utf-8 -*-

from redap.specs.user import ldap_operation_spec
from redap.specs.descriptions import USER_UNLOCK
from copy import deepcopy

user_unlock = deepcopy(ldap_operation_spec)
user_unlock['summary'] = USER_UNLOCK

# -*- coding: utf-8 -*-

from lapdance.specs.user import ldap_operation_spec
from lapdance.specs.descriptions import USER_DISABLE
from copy import deepcopy

user_disable = deepcopy(ldap_operation_spec)
user_disable['summary'] = USER_DISABLE

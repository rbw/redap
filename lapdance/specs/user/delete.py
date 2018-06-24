# -*- coding: utf-8 -*-

from lapdance.specs.user import ldap_operation_spec
from lapdance.specs.descriptions import USER_DELETE
from copy import deepcopy

user_delete = deepcopy(ldap_operation_spec)
user_delete['summary'] = USER_DELETE

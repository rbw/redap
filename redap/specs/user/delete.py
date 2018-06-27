# -*- coding: utf-8 -*-

from redap.specs.user import ldap_operation_spec
from redap.specs.descriptions import USER_DELETE
from copy import deepcopy

user_delete = deepcopy(ldap_operation_spec)
user_delete['summary'] = USER_DELETE

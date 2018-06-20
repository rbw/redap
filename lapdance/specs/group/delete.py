# -*- coding: utf-8 -*-

from lapdance.specs.group import ldap_operation_spec
from lapdance.specs.constants import GROUP_DELETE
from copy import deepcopy

group_delete = deepcopy(ldap_operation_spec)
group_delete['summary'] = GROUP_DELETE

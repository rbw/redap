# -*- coding: utf-8 -*-

from .schemas import default_profiles, container_schema, core_schema, ldap_schema
from .loader import SchemaLoader, CoreLoader, LDAPLoader


ldap = LDAPLoader('ldap.yml')
core = CoreLoader('core.yml')

user_schema = SchemaLoader('user.yml', ldap.base_dn, ldap.dirtype)
group_schema = SchemaLoader('group.yml', ldap.base_dn, ldap.dirtype)


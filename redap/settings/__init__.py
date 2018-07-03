# -*- coding: utf-8 -*-

from .schemas import default_profiles, container_schema, core_schema, ldap_schema
from .loader import SchemaLoader, CoreLoader, LDAPLoader


ldap = LDAPLoader(file_name='ldap.yml')
core = CoreLoader(file_name='core.yml')

user_schema = SchemaLoader(file_name='user.yml', base_dn=ldap.base_dn, dirtype=ldap.dirtype)
group_schema = SchemaLoader(file_name='group.yml', base_dn=ldap.base_dn, dirtype=ldap.dirtype)


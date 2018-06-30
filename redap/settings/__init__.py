from .loader import UserLoader, GroupLoader, CoreLoader, LDAPLoader

ldap = LDAPLoader()
core = CoreLoader()

_dirtype = ldap.data['directory_type']

user_schema = UserLoader(dirtype=_dirtype)
group_schema = GroupLoader(dirtype=_dirtype)

# -*- coding: utf-8 -*-

from ldap3 import MODIFY_REPLACE
from lapdance.models import LDAPUser
from .base import Service, VENDOR_MICROSOFT

# UserAccountControl flags
UAC_PW_NEVER_EXPIRES = 66048
UAC_ENABLE = 512
UAC_DISABLE = 514


class UserService(Service):
    __model__ = LDAPUser
    __config_name__ = 'LAPDANCE_LDAP_USER'

    def _set_account_control(self, user_id, flag):
        user = self.get_one(user_id)
        user.userAccountControl = [(MODIFY_REPLACE, [flag])]

    def is_member_of(self, user_dn, group_dn):
        id_attr = self.config['fields']['id']['ldap_name']
        return len(self.get_many('({0}={1})(memberOf={2})'.format(id_attr, user_dn, group_dn))) > 0

    def get_groups(self, user_id, include_nested=False, **kwargs):
        """Imports groups service and obtains a list of groups for the user"""

        from lapdance.services import groups

        user_dn = self.get_one(user_id).dn

        if include_nested in [str(1), 'true']:
            self._raise_if_incompatible_with(VENDOR_MICROSOFT)
            nested_filter = '(member:1.2.840.113556.1.4.1941:={0})'.format(user_dn)
        else:
            nested_filter = '(member={0})'.format(user_dn)

        return groups.get_many(nested_filter, **kwargs)

    def set_password(self, user_id, **kwargs):
        user = self.get_one(user_id)
        self._microsoft_ext.modify_password(user.dn, **kwargs)

    def unlock(self, user_id):
        self._microsoft_ext.unlock_account(self.get_one(user_id).dn)

    def pw_never_expires(self, user_id):
        self._set_account_control(user_id, UAC_PW_NEVER_EXPIRES)

    def enable(self, user_id):
        self._set_account_control(user_id, UAC_ENABLE)

    def disable(self, user_id):
        self._set_account_control(user_id, UAC_DISABLE)

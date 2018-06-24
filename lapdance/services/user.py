# -*- coding: utf-8 -*-

from ldap3 import MODIFY_REPLACE, MODIFY_ADD
from ldap3.core.exceptions import LDAPOperationResult
from lapdance.models import LDAPUser
from lapdance.core import ldap
from lapdance.exceptions import LapdanceError
from .base import Service, ACTIVE_DIRECTORY

# UserAccountControl flags
UAC_PW_NEVER_EXPIRES = 66048
UAC_ENABLE = 512
UAC_DISABLE = 514


class UserService(Service):
    __model__ = LDAPUser
    __config_name__ = 'LAPDANCE_LDAP_USER'

    def _set_account_control(self, user_id, flag):
        self._raise_if_incompatible_with(ACTIVE_DIRECTORY)
        payload = {'userAccountControl': [(MODIFY_REPLACE, [flag])]}
        self.conn.modify(dn=self.get_one(user_id).dn,
                         changes=payload)

    def is_member_of(self, user_dn, group_dn):
        id_attr = self.config['fields']['id']['ref']
        return len(self.get_many(filter='({0}={1})(memberOf={2})'.format(id_attr, user_dn, group_dn))) > 0

    @property
    def _groups(self):
        from lapdance.services import groups
        return groups

    def get_groups(self, user_id, include_nested=False, **kwargs):
        user_dn = self.get_one(user_id).dn

        if str(include_nested).lower() in [str(1), 'true']:
            self._raise_if_incompatible_with(ACTIVE_DIRECTORY)
            kwargs['filter'] = '(member:1.2.840.113556.1.4.1941:={0})'.format(user_dn)
        else:
            kwargs['filter'] = '(member={0})'.format(user_dn)

        return self._groups.get_many(**kwargs)

    def authenticate(self, username, password):
        user_dn = self.get_one(username).dn

        try:
            conn = ldap.connect(user_dn, password)
            conn.unbind()
        except LDAPOperationResult as e:
            if e.description == 'invalidCredentials':
                raise LapdanceError(message='Invalid username or password', status_code=401)
            else:
                raise

        return True

    def set_password(self, user_id, **kwargs):
        user = self.get_one(user_id)

        if self.dirtype == ACTIVE_DIRECTORY:
            self._microsoft_ext.modify_password(user.dn, **kwargs)
        else:
            self.conn.extend.standard.modify_password(user.dn, **kwargs)

    def unlock(self, user_id):
        self._microsoft_ext.unlock_account(self.get_one(user_id).dn)

    def pw_never_expires(self, user_id):
        self._set_account_control(user_id, UAC_PW_NEVER_EXPIRES)

    def enable(self, user_id):
        self._set_account_control(user_id, UAC_ENABLE)

    def disable(self, user_id):
        self._set_account_control(user_id, UAC_DISABLE)

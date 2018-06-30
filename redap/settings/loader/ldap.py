# -*- coding: utf-8 -*-

from urllib.parse import urlparse
from .base import Loader
from redap.settings.schemas import ldap_schema


class LDAPLoader(Loader):
    def __init__(self, file_name='ldap.yml', **kwargs):
        super(LDAPLoader, self).__init__(file_name, schema=ldap_schema, **kwargs)
        uri = urlparse(self.data.pop('uri'))
        self._data['hostname'] = uri.hostname
        self._data['port'] = uri.port
        self._data['use_ssl'] = True if uri.scheme == 'ldaps' else False

    @property
    def base_dn(self):
        return self.data['base_dn']

    @property
    def dirtype(self):
        return self.data['directory_type']

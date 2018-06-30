# -*- coding: utf-8 -*-

import os
import yaml
import json
from functools import lru_cache
from urllib.parse import urlparse
from cerberus import Validator
from redap.exceptions import InvalidConfiguration

from .schemas import default_profiles, container_schema, core_schema, ldap_schema


class Loader(object):
    def __init__(self, file, **kwargs):
        self.dirtype = kwargs.pop('dirtype', None)
        self.schema = kwargs.pop('schema', None)

        directory = kwargs.pop('directory', os.environ.get('REDAP_SETTINGS_DIR', 'settings'))
        self.file = file
        self.file_path = '{0}/{1}'.format(directory, file)

        self.data = self._open(self.file_path)

        if self.dirtype and default_profiles[self.dirtype].get(self.file):
            self._apply_profile(default_profiles[self.dirtype][self.file])

        if self.schema:
            self.data = self._validate(self.data, self.schema)

    def _apply_profile(self, profile):
        def _is_empty(value):
            if (
                isinstance(value, str) and not value
                or
                isinstance(value, list) and len(value) == 0
            ):
                return True

            return False

        for k, v in profile.items():
            # Set value from profile if empty
            if k not in self.data or _is_empty(self.data[k]):
                self.data[k] = v

    def _validate(self, data, schema):
        v = Validator(schema)
        v.allow_unknown = True
        v.validate(data, schema)
        if v.errors:
            raise InvalidConfiguration(self.file_path, json.dumps(v.errors, indent=4, separators=(',', ': ')))

        return v.__dict__['document']

    @lru_cache()
    def _open(self, file_path):
        with open(file_path, 'r') as stream:
            try:
                return yaml.load(stream) or {}
            except yaml.YAMLError as exception:
                raise exception


class CoreLoader(Loader):
    def __init__(self, **kwargs):
        super(CoreLoader, self).__init__('core.yml', schema=core_schema, **kwargs)


class LDAPLoader(Loader):
    def __init__(self, **kwargs):
        super(LDAPLoader, self).__init__('ldap.yml', schema=ldap_schema, **kwargs)
        if 'uri' in self.data:
            uri = urlparse(self.data.pop('uri'))
            self.data['hostname'] = uri.hostname
            self.data['port'] = uri.port
            self.data['use_ssl'] = True if uri.scheme == 'ldaps' else False


class UserLoader(Loader):
    def __init__(self, **kwargs):
        super(UserLoader, self).__init__('user.yml', schema=container_schema, **kwargs)


class GroupLoader(Loader):
    def __init__(self, **kwargs):
        super(GroupLoader, self).__init__('group.yml', schema=container_schema, **kwargs)


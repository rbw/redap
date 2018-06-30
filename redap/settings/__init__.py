# -*- coding: utf-8 -*-

from functools import lru_cache
from urllib.parse import urlparse
from redap.settings.schemas.profiles import defaults
from .schemas import container_schema, core_schema, ldap_schema
from .utils import load_doc
import os
import yaml
import json
from cerberus import Validator
from redap.exceptions import InvalidConfiguration


class Settings(object):
    dirtype = None

    def __init__(self, file, directory=None, schema=None):
        directory = directory or os.environ.get('REDAP_SETTINGS_DIR', 'settings')
        self.file_path = '{0}/{1}'.format(directory, file)
        self.schema = schema

        if self.dirtype in defaults and defaults[self.dirtype]:
            self._apply_profile(defaults[self.dirtype])

        if self.schema:
            self._validate(self.schema)

    @property
    def data(self):
        return self._open(self.file_path)

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

    def _validate(self, schema=None):
        v = Validator(schema)
        v.allow_unknown = True
        v.validate(self.data, schema)
        if v.errors:
            raise InvalidConfiguration(self.file_path, json.dumps(v.errors, indent=4, separators=(',', ': ')))

    @lru_cache()
    def _open(self, file_path):
        with open(file_path, 'r') as stream:
            try:
                return yaml.load(stream) or {}
            except yaml.YAMLError as exception:
                raise exception


class CoreSettings(Settings):
    def __init__(self, **kwargs):
        super(CoreSettings, self).__init__('core.yml', schema=core_schema, **kwargs)


class LDAPSettings(Settings):
    def __init__(self, **kwargs):
        super(LDAPSettings, self).__init__('ldap.yml', schema=ldap_schema, **kwargs)

    @lru_cache()
    def __dict__(self):
        d = self.data
        if 'uri' in d:
            uri = urlparse(d.pop('uri'))
            d['hostname'] = uri.hostname
            d['port'] = uri.port
            d['use_ssl'] = True if uri.scheme == 'ldaps' else False

        return d


class UserSchema(Settings):
    def __init__(self, **kwargs):
        print(self.dirtype)
        super(UserSchema, self).__init__('user.yml', schema=container_schema, **kwargs)


class GroupSchema(Settings):
    def __init__(self, **kwargs):
        super(GroupSchema, self).__init__('group.yml', schema=container_schema, **kwargs)


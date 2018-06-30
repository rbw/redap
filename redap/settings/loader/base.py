# -*- coding: utf-8 -*-

import os
import yaml
import json
from functools import lru_cache
from cerberus import Validator
from redap.exceptions import InvalidConfiguration

SETTINGS_DIR_ENV = 'REDAP_SETTINGS_DIR'
DEFAULT_SETTINGS_DIR = 'settings'


class Loader(object):
    def __init__(self, file_name, directory=None, data=None, **kwargs):
        self.schema = kwargs.pop('schema', None)
        self.directory = directory
        self.file_name = file_name
        self._data = data or self._open(self.file_name)

    @property
    def data(self):
        if self.schema:
            return self._validate(self._data, self.schema)

        return self._data

    def _validate(self, data, schema):
        v = Validator(schema)
        v.allow_unknown = True
        v.validate(data, schema)
        if v.errors:
            raise InvalidConfiguration(self.file_name, json.dumps(v.errors, indent=4, separators=(',', ': ')))

        return v.__dict__['document']

    @lru_cache()
    def _open(self, file_name):
        directory = os.environ.get(SETTINGS_DIR_ENV, DEFAULT_SETTINGS_DIR)
        file_path = '{0}/{1}'.format(directory, file_name)

        with open(file_path, 'r') as stream:
            try:
                return yaml.load(stream) or {}
            except yaml.YAMLError as exception:
                raise exception




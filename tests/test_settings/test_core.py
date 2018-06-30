# -*- coding: utf-8 -*-

from unittest import TestCase
from redap.settings.loader import CoreLoader
from redap.exceptions import InvalidConfiguration
from copy import copy

DEFAULT_AUTH_TYPE = 'disabled'
DEFAULT_DATABASE_URI = 'sqlite+pysqlite:///.redap.db'

CONFIG_BASE = {
    'auth_type': 'api_key',
    'database_uri': 'test'
}


class SettingsLoaderCase(TestCase):
    """Invalid auth_type should raise InvalidConfiguration"""
    def test_auth_type_enum(self):
        c = copy(CONFIG_BASE)
        c['auth_type'] = 'Invalid'

        self.assertRaises(InvalidConfiguration, CoreLoader, data=c)

    """No auth_type should set default"""
    def test_auth_type_default(self):
        c = copy(CONFIG_BASE)
        del c['auth_type']

        data = CoreLoader(data=c).data
        self.assertEqual(data['auth_type'], DEFAULT_AUTH_TYPE)

    """No database_uri should set default"""
    def test_no_database_uri(self):
        c = copy(CONFIG_BASE)
        del c['database_uri']

        data = CoreLoader(data=c).data
        self.assertEqual(data['database_uri'], DEFAULT_DATABASE_URI)

    """Setting a valid config should work"""
    def test_valid(self):
        data = CoreLoader(data=CONFIG_BASE).data
        self.assertEqual(data['database_uri'], CONFIG_BASE['database_uri'])
        self.assertEqual(data['auth_type'], CONFIG_BASE['auth_type'])

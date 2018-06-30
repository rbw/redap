# -*- coding: utf-8 -*-

from unittest import TestCase
from redap.settings.loader import UserLoader
from redap.exceptions import InvalidConfiguration
from copy import copy

DEFAULT_HIDDEN_FIELDS = []
DEFAULT_REQUIRED_FIELDS = []

RELATIVE_DN = 'ou=users'

CLASSES = [
    'top',
    'person',
    'organizationalPerson',
    'user',
]

HIDDEN_FIELDS = [
    'distinguished_name'
]

REQUIRED_FIELDS = [
    'id', 'email', 'name', 'last_name', 'first_name'
]

FIELDS = {
    'id': {
        'type': 'string',
        'ref': 'sAMAccountName'
    },
    'name': {
        'type': 'string',
        'ref': 'cn'
    },
    'email': {
        'type': 'string',
        'ref': 'mail'
    }
}

CONFIG_BASE = {
    'relative_dn': RELATIVE_DN,
    'classes': CLASSES,
    'hidden_fields': HIDDEN_FIELDS,
    'required_fields': REQUIRED_FIELDS,
    'fields': FIELDS
}


class SettingsLoaderCase(TestCase):
    """Setting a valid custom schema should work"""
    def test_valid_schema(self):
        schema = UserLoader(data=CONFIG_BASE).data

        self.assertEqual(schema['relative_dn'], RELATIVE_DN)
        self.assertEqual(schema['classes'], CLASSES)
        self.assertEqual(schema['hidden_fields'], HIDDEN_FIELDS)
        self.assertEqual(schema['required_fields'], REQUIRED_FIELDS)
        self.assertEqual(schema['fields'], FIELDS)

    """Missing relative_dn should fail"""
    def test_missing_relative_dn(self):
        c = copy(CONFIG_BASE)
        del c['relative_dn']

        self.assertRaises(InvalidConfiguration, UserLoader, data=c)

    """Missing classes should fail"""
    def test_missing_classes(self):
        c = copy(CONFIG_BASE)
        del c['classes']

        self.assertRaises(InvalidConfiguration, UserLoader, data=c)

    """Missing fields should fail"""
    def test_missing_fields(self):
        c = copy(CONFIG_BASE)
        del c['fields']

        self.assertRaises(InvalidConfiguration, UserLoader, data=c)

    """Missing required_fields should set its default value"""
    def test_required_fields_default(self):
        c = copy(CONFIG_BASE)
        del c['required_fields']

        schema = UserLoader(data=c).data

        self.assertEqual(schema['required_fields'], DEFAULT_REQUIRED_FIELDS)

    """Missing required_fields should set its default value"""
    def test_hidden_fields_default(self):
        c = copy(CONFIG_BASE)
        del c['hidden_fields']

        schema = UserLoader(data=c).data

        self.assertEqual(schema['hidden_fields'], DEFAULT_HIDDEN_FIELDS)

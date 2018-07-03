# -*- coding: utf-8 -*-

from unittest import TestCase
from redap.settings.loader import LDAPLoader
from redap.exceptions import InvalidConfiguration
from copy import copy

HOST_NAME = 'foo.bar'
PORT = 636
BASE_DN = 'dc=demo1,dc=freeipa,dc=org'
BIND_DN = 'uid=admin,cn=users,cn=accounts,dc=demo1,dc=freeipa,dc=org'
SECRET = 'Secret123'
RETURN_ERROR_DETAILS = True

DEFAULT_DIRECTORY_TYPE = 'custom'
DEFAULT_RETURN_ERRORS = False
DEFAULT_CONN_TIMEOUT = 3

CONFIG_BASE = {
    'uri': 'ldaps://{0}:{1}'.format(HOST_NAME, PORT),
    'base_dn': BASE_DN,
    'conn_timeout': DEFAULT_CONN_TIMEOUT,
    'bind_dn': BIND_DN,
    'secret': SECRET,
    'return_error_details': RETURN_ERROR_DETAILS
}


def get_ldap(data, **kwargs):
    return LDAPLoader(data=data, **kwargs).data


class SettingsLoaderCase(TestCase):
    """Setting a valid configuration should work"""
    def test_set_valid_config(self):
        c = copy(CONFIG_BASE)
        data = get_ldap(c)

        self.assertEqual(data['base_dn'], BASE_DN)
        self.assertEqual(data['conn_timeout'], DEFAULT_CONN_TIMEOUT)
        self.assertEqual(data['bind_dn'], BIND_DN)
        self.assertEqual(data['secret'], SECRET)
        self.assertEqual(data['return_error_details'], RETURN_ERROR_DETAILS)

    """Setting use_ssl by LDAP schema should work"""
    def test_set_ssl_by_schema(self):
        c = copy(CONFIG_BASE)

        data = get_ldap(c)
        self.assertTrue(data['use_ssl'])

        c['uri'] = 'ldap://foo.bar:636'

        data = get_ldap(c)
        self.assertFalse(data['use_ssl'])

    """Extracting host_name from URI should work"""
    def test_get_host_name(self):
        data = get_ldap(CONFIG_BASE)
        self.assertEqual(data['hostname'], HOST_NAME)

    """Extracting port from URI should work"""
    def test_get_port(self):
        data = get_ldap(CONFIG_BASE)
        self.assertEqual(data['port'], PORT)

    """Not setting a conn_timeout should set its default"""
    def test_default_conn_timeout(self):
        c = copy(CONFIG_BASE)
        del c['conn_timeout']

        data = get_ldap(c)
        self.assertEqual(data['conn_timeout'], 3)

    """Not setting a directory_type should set its default"""
    def test_default_directory_type(self):
        c = copy(CONFIG_BASE)
        data = get_ldap(c)
        self.assertEqual(data['directory_type'], DEFAULT_DIRECTORY_TYPE)

    """Not setting a return_error_details should set its default"""
    def test_default_return_errors(self):
        c = copy(CONFIG_BASE)
        del c['return_error_details']

        data = get_ldap(c)
        self.assertEqual(data['return_error_details'], DEFAULT_RETURN_ERRORS)

    """Not specifying a base_dn should fail"""
    def test_missing_base_dn(self):
        c = copy(CONFIG_BASE)
        del c['base_dn']

        self.assertRaises(InvalidConfiguration, get_ldap, c)

    """Not specifying a bind_dn should fail"""
    def test_missing_bind_dn(self):
        c = copy(CONFIG_BASE)
        del c['bind_dn']

        self.assertRaises(InvalidConfiguration, get_ldap, c)

    """Not specifying a secret should fail"""
    def test_missing_secret(self):
        c = copy(CONFIG_BASE)
        del c['secret']

        self.assertRaises(InvalidConfiguration, get_ldap, c)


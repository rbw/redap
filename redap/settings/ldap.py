# -*- coding: utf-8 -*-

import ssl
from ldap3.utils.log import set_library_log_detail_level, OFF, ERROR, BASIC, NETWORK, EXTENDED, PROTOCOL
from . import ldap

ldap_settings = ldap.data

REDAP_BASE_DN = ldap_settings['base_dn']
REDAP_LDAP_DIRTYPE = ldap_settings['directory_type']

# Return LDAP error details to client
REDAP_SHOW_LDAP_ERROR_DETAILS = ldap_settings['return_error_details']

LDAP_SERVER = ldap_settings['hostname']
LDAP_PORT = ldap_settings['port']
LDAP_BINDDN = ldap_settings['bind_dn']
LDAP_SECRET = ldap_settings['secret']
LDAP_USE_SSL = ldap_settings['use_ssl']
LDAP_CONNECT_TIMEOUT = ldap_settings['conn_timeout']
LDAP_REQUIRE_CERT = ssl.CERT_NONE
LDAP_USE_TLS = False
LDAP_RAISE_EXCEPTIONS = True
FORCE_ATTRIBUTE_VALUE_AS_LIST = True

# LDAP3 Log-level
log_level_mappings = {
    'off': OFF,
    'error': ERROR,
    'basic': BASIC,
    'protocol': PROTOCOL,
    'network': NETWORK,
    'extended': EXTENDED
}

set_library_log_detail_level(log_level_mappings[ldap_settings['debug']])


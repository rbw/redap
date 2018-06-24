# -*- coding: utf-8 -*-

import ssl
from ldap3.utils.log import set_library_log_detail_level, OFF, BASIC, NETWORK, EXTENDED
from .loader import user_settings, group_settings, ldap_settings

LAPDANCE_BASE_DN = ldap_settings['base_dn']
LAPDANCE_LDAP_DIRTYPE = ldap_settings['directory_type']
LAPDANCE_LDAP_USER = user_settings
LAPDANCE_LDAP_GROUP = group_settings

# Return LDAP error details to client
LAPDANCE_SHOW_LDAP_ERROR_DETAILS = ldap_settings['return_error_details']

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
    'basic': BASIC,
    'network': NETWORK,
    'extended': EXTENDED
}

set_library_log_detail_level(log_level_mappings[ldap_settings['debug']])


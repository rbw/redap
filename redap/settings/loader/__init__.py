# -*- coding: utf-8 -*-

from urllib.parse import urlparse
from redap.settings.schemas import container_schema, core_schema, ldap_schema
from .utils import load_doc
from .profiles import defaults


LDAP_SETTINGS_FILE = 'settings/ldap.yml'
CORE_SETTINGS_FILE = 'settings/core.yml'
USER_SETTINGS_DOC = 'settings/user.yml'
GROUP_SETTINGS_FILE = 'settings/group.yml'

ldap_settings = load_doc(LDAP_SETTINGS_FILE, ldap_schema)
dir_defaults = defaults[ldap_settings['directory_type']]

files_schemas = [
    (CORE_SETTINGS_FILE, core_schema, None),
    (USER_SETTINGS_DOC, container_schema, dir_defaults['user']),
    (GROUP_SETTINGS_FILE, container_schema, dir_defaults['group']),
]

# Create and validate configuration objects from YAML
(
    core_settings,
    user_settings,
    group_settings
) = [load_doc(doc, schema, defaults) for doc, schema, defaults in files_schemas]


uri = urlparse(ldap_settings.pop('uri'))
ldap_settings['hostname'] = uri.hostname
ldap_settings['port'] = uri.port
ldap_settings['use_ssl'] = True if uri.scheme == 'ldaps' else False


# -*- coding: utf-8 -*-
from urllib.parse import urlparse
from lapdance.settings.schemas import container_schema, core_schema, ldap_schema
from .utils import load_doc


LDAP_SETTINGS_FILE = 'settings/ldap.yaml'
CORE_SETTINGS_FILE = 'settings/core.yaml'
USER_SETTINGS_DOC = 'settings/user.yaml'
GROUP_SETTINGS_FILE = 'settings/group.yaml'

files_schemas = [
    (CORE_SETTINGS_FILE, core_schema),
    (LDAP_SETTINGS_FILE, ldap_schema),
    (USER_SETTINGS_DOC, container_schema),
    (GROUP_SETTINGS_FILE, container_schema),
]

# Create and validate configuration objects from YAML
(
    core_settings,
    ldap_settings,
    user_settings,
    group_settings
) = [load_doc(doc, schema) for doc, schema in files_schemas]


uri = urlparse(ldap_settings.pop('uri'))
ldap_settings['hostname'] = uri.hostname
ldap_settings['port'] = uri.port
ldap_settings['use_ssl'] = True if uri.scheme == 'ldaps' else False

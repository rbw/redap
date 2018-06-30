# -*- coding: utf-8 -*-

from urllib.parse import urlparse
from redap.settings.schemas import container_schema, core_schema, ldap_schema
from redap.settings.schemas.profiles import defaults
from .utils import load_doc


ldap_settings = load_doc('ldap.yml', ldap_schema)
dir_defaults = defaults[ldap_settings['directory_type']]

files_schemas = [
    ('core.yml', core_schema, None),
    ('user.yml', container_schema, dir_defaults['user']),
    ('group.yml', container_schema, dir_defaults['group']),
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


# -*- coding: utf-8 -*-

schema = {
    'uri': {
        'required': True,
        'type': 'string',
        'regex': '(ldaps?://)(([^:^/]*):[0-9]+)'
    },
    'base_dn': {
        'required': True,
        'type': 'string',
    },
    'bind_dn': {
        'required': True,
        'type': 'string',
    },
    'conn_timeout': {
        'required': False,
        'type': 'integer',
        'default': 3,
    },
    'directory_type': {
        'required': False,
        'type': 'string',
        'allowed': ['ad', 'freeipa', 'custom'],
        'default': 'custom'
    },
    'secret': {
        'required': True,
        'type': 'string',
    },
    'debug': {
        'required': False,
        'type': 'string',
        'allowed': ['off', 'basic', 'network', 'extended'],
        'default': 'off'
    },
    'return_error_details': {
        'required': False,
        'type': 'boolean',
        'default': False,
    },
}

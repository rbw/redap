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
    'secret': {
        'required': True,
        'type': 'string',
    },
    'debug': {
        'required': False,
        'type': 'string',
        'allowed': ['disabled', 'basic', 'network', 'extended'],
        'default': 'disabled',
    },
    'return_error_details': {
        'required': False,
        'type': 'boolean',
        'default': False,
    },
}

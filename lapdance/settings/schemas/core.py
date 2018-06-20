# -*- coding: utf-8 -*-

schema = {
    'auth_type': {
        'default': 'disabled',
        'type': 'string',
        'allowed': ['api_key', 'disabled'],
    },
    'database_uri': {
        'required': True,
        'type': 'string',
        'default': 'sqlite+pysqlite:///.lapdance.db',
    }
}

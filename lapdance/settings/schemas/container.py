# -*- coding: utf-8 -*-

schema = {
    'classes': {
        'required': True,
        'type': 'list',
        'default': []
    },
    'default_filter': {
        'required': False,
        'default': '(cn=*)',
        'type': 'string'
    },
    'relative_dn': {
        'required': False,
        'type': 'string'
    },
    'hidden_fields': {
        'required': False,
        'type': 'list',
        'default': []
    },
    'required_fields': {
        'required': False,
        'type': 'list',
        'default': []
    },
    'fields': {
        'type': 'dict',
        'allow_unknown': True,
        'valueschema': {
            'type': 'dict',
            'schema': {
                'ldap_name': {
                    'type': 'string',
                    'required': True
                },
                'type': {
                    'type': 'string',
                    'required': True
                },
            }
        },
        'schema': {
            'id': {
                'type': 'dict',
                'required': True,
            },
        },
    }
}

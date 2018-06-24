# -*- coding: utf-8 -*-

schema = {
    'classes': {
        'required': True,
        'type': 'list',
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
        'required': True,
        'valueschema': {
            'type': 'dict',
            'schema': {
                'ref': {
                    'type': 'string',
                    'required': True
                },
                'type': {
                    'type': 'string',
                    'required': True
                },
                'default': {
                    'required': False
                }
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

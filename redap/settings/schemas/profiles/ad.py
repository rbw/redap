# -*- coding: utf-8 -*-

defaults_ad = {
    'group.yml': {
        'classes': [
            'top',
            'group',
        ],
        'hidden_fields': [
            'distinguished_name'
        ],
        'required_fields': [
            'id', 'description'
        ],
        'fields': {
            'id': {
                'type': 'string',
                'ref': 'cn'
            },
            'created_at': {
                'type': 'string',
                'ref': 'whenCreated'
            },
            'updated_at': {
                'type': 'string',
                'ref': 'whenChanged'
            },
            'distinguished_name': {
                'type': 'string',
                'ref': 'distinguishedName'
            },
            'description': {
                'type': 'string',
                'ref': 'description'
            },
        }
    },
    'user.yml': {
        'classes': [
            'top',
            'person',
            'organizationalPerson',
            'user',
        ],
        'hidden_fields': [
            'distinguished_name'
        ],
        'required_fields': [
            'id', 'email', 'name', 'last_name', 'first_name'
        ],
        'fields': {
            'id': {
                'type': 'string',
                'ref': 'sAMAccountName'
            },
            'name': {
                'type': 'string',
                'ref': 'cn'
            },
            'email': {
                'type': 'string',
                'ref': 'mail'
            },
            'distinguished_name': {
                'type': 'string',
                'ref': 'distinguishedName'
            },
            'last_name': {
                'type': 'string',
                'ref': 'sn'
            },
            'first_name': {
                'type': 'string',
                'ref': 'givenName'
            },
            'last_logon': {
                'type': 'integer',
                'ref': 'lastLogon',
            },
            'logon_count': {
                'type': 'integer',
                'ref': 'logonCount',
            },
            'created_at': {
                'type': 'string',
                'ref': 'whenCreated',
            },
            'updated_at': {
                'type': 'string',
                'ref': 'whenChanged',
            }
        }
    }
}

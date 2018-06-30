# -*- coding: utf-8 -*-

defaults_freeipa = {
    'group': {
        'classes': [
            'top',
            'groupofnames',
            'nestedgroup',
            'posixGroup',
            'ipausergroup',
            'ipaobject'
        ],
        'hidden_fields': [
            'gid_number'
        ],
        'required_fields': [
            'id', 'description'
        ],
        'fields': {
            'id': {
                'type': 'id',
                'ref': 'cn'
            },
            'gid_number': {
                'type': 'integer',
                'ref': 'gidNumber',
                'default': -1,
            },
            'description': {
                'type': 'string',
                'ref': 'description'
            },
        }
    },
    'user': {
        'classes': [
            'top',
            'inetorgperson',
            'person',
            'organizationalperson',
            'inetuser',
            'posixaccount',
            'ipaobject',
        ],
        'hidden_fields': [
            'uid_number', 'gid_number'
        ],
        'required_fields': [
            'id', 'home', 'shell', 'name', 'email', 'last_name', 'first_name'
        ],
        'fields': {
            'id': {
                'type': 'id',
                'ref': 'uid',
            },
            'uid_number': {
                'type': 'integer',
                'ref': 'uidNumber',
                'default': -1,
            },
            'gid_number': {
                'type': 'integer',
                'ref': 'gidNumber',
                'default': -1,
            },
            'home': {
                'type': 'string',
                'ref': 'homedirectory',
            },
            'shell': {
                'type': 'string',
                'ref': 'loginshell',
            },
            'name': {
                'type': 'string',
                'ref': 'cn'
            },
            'email': {
                'type': 'string',
                'ref': 'mail'
            },
            'last_name': {
                'type': 'string',
                'ref': 'sn'
            },
            'first_name': {
                'type': 'string',
                'ref': 'givenName'
            }
        }
    }
}

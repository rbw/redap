# -*- coding: utf-8 -*-

defaults_freeipa = {
    'group': {
        'classes': [
            'top',
            'groupofnames',
            'nestedgroup',
            'ipausergroup',
            'ipaobject'
        ],
        'required_fields': [
            'id', 'name'
        ],
        'fields': {
            'id': {
                'type': 'string',
                'ldap_name': 'cn'
            },
            'gid': {
                'type': 'integer',
                'ldap_name': 'gidNumber'
            },
            'description': {
                'type': 'string',
                'ldap_name': 'description'
            },
        }
    },
    'user': {
        'classes': [
            'top',
            'person',
            'organizationalperson',
            'inetorgperson',
            'inetuser',
            'posixaccount',
            'ipaobject',
        ],
        'required_fields': [
            'id', 'gid', 'uidNumber', 'name', 'first_name', 'last_name',
            'shell', 'home', 'email'
        ],
        'fields': {
            'id': {
                'type': 'string',
                'ldap_name': 'uid'
            },
            'uidNumber': {
                'type': 'integer',
                'ldap_name': 'uidNumber'
            },
            'gid': {
                'type': 'integer',
                'ldap_name': 'gidNumber'
            },
            'home': {
                'type': 'string',
                'ldap_name': 'homedirectory'
            },
            'shell': {
                'type': 'string',
                'ldap_name': 'loginshell',
            },
            'name': {
                'type': 'string',
                'ldap_name': 'cn'
            },
            'email': {
                'type': 'string',
                'ldap_name': 'mail'
            },
            'last_name': {
                'type': 'string',
                'ldap_name': 'sn'
            },
            'first_name': {
                'type': 'string',
                'ldap_name': 'givenName'
            }
        }
    }
}

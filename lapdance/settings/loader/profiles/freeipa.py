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
        'relative_dn': 'cn=groups,cn=accounts',
        'fields': {
            'id': {
                'type': 'string',
                'ldap_name': 'cn'
            },
            'gid_number': {
                'type': 'integer',
                'ldap_name': 'gidNumber',
                'default': -1,
                'required': False,
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
            'inetorgperson',
            'person',
            'organizationalperson',
            'inetuser',
            'posixaccount',
            'ipaobject',
        ],
        'relative_dn': 'cn=users,cn=accounts',
        'fields': {
            'id': {
                'type': 'string',
                'ldap_name': 'uid',
            },
            'uid_number': {
                'type': 'integer',
                'ldap_name': 'uidNumber',
                'default': -1,
                'required': False,
            },
            'gid_number': {
                'type': 'integer',
                'ldap_name': 'gidNumber',
                'default': -1,
                'required': False,
            },
            'home': {
                'type': 'string',
                'ldap_name': 'homedirectory',
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

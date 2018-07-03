# -*- coding: utf-8 -*-

LDAP_OPERATION = {
    'definition': {
        'LDAPOperation': {
            'type': 'object',
            'properties': {
                'result': {
                    'type': 'string'
                }
            }
        }
    },
    'response': {
        'description': 'LDAP operation',
        'schema': {
            '$ref': '#/definitions/LDAPOperation'
        },
    }
}

ERROR_DEFINITIONS = {
    'InputError': {
        'type': 'object',
        'properties': {
            'code': {
                'type': 'integer'
            },
            'message': {
                'type': 'string'
            },
        }
    },
    'LDAPError': {
        'type': 'object',
        'properties': {
            'code': {
                'type': 'integer',
            },
            'message': {
                'type': 'object',
                'properties': {
                    'description': {
                        'type': 'string'
                    },
                    'message': {
                        'type': 'string'
                    },
                    'result': {
                        'type': 'integer'
                    },
                    'type': {
                        'type': 'string'
                    }
                }
            }
        }
    }
}

ERROR_RESPONSES = {
    '400': {
        'description': 'Input error',
        'schema': {
            '$ref': '#/definitions/InputError'
        },
    },
    '500': {
        'description': 'LDAP error',
        'schema': {
            '$ref': '#/definitions/LDAPError'
        }
    }
}



# -*- coding: utf-8 -*-

RESPONSES = {
    '201': {
        'description': 'Operation result',
        'schema': {
            '$ref': '#/definitions/ResponseSuccess'
        },
    },
    '400': {
        'description': 'Operational error',
        'schema': {
            '$ref': '#/definitions/OperationError'
        },
    },
    '500': {
        'description': 'LDAP error',
        'schema': {
            '$ref': '#/definitions/LDAPError'
        },
    }
}

DEFINITIONS = {
        'ResponseSuccess': {
            'type': 'object',
            'properties': {
                'result': {
                    'type': 'string'
                }
            }
        },
        'OperationError': {
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
        'LDAPOperationError': {
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
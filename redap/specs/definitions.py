# -*- coding: utf-8 -*-

BASE_RESPONSES = {
    '201': {
        'description': 'Operation result',
        'schema': {
            '$ref': '#/definitions/ResponseSuccess'
        },
    },
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
        },
    }
}

PASSWORD_CHANGE = {
    'PasswordChange': {
        'type': 'object',
        'required': ['new_password'],
        'properties': {
            'new_password': {
                'type': 'string'
            },
            'old_password': {
                'type': 'string'
            }
        }
    }
}

CREDENTIALS = {
    'Credentials': {
        'type': 'object',
        'required': ['username', 'password'],
        'properties': {
            'username': {
                'type': 'string'
            },
            'password': {
                'type': 'string'
            }
        }
    }
}

MEMBER_ADD = {
    'MemberAdd': {
        'required': ['id'],
        'properties': {
            'id': {
                'type': 'string',
                'description': 'User id',
                'example': 'monty.python'
            },
            'fix': {
                'type': 'string',
                'default': False,
                'description': 'Add even if already relationship already exists'
            }
        }
    }
}


BASE_DEFINITIONS = {
    'ResponseSuccess': {
        'type': 'object',
        'properties': {
            'result': {
                'type': 'string'
            }
        }
    },
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
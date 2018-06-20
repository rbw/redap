# -*- coding: utf-8 -*-

many_filter_param = {
    'name': 'filter',
    'in': 'query',
    'type': 'string',
    'required': False
}

op_success_def = {
    'ResponseSuccess': {
        'type': 'object',
        'properties': {
            'result': {
                'type': 'string'
            }
        }
    }
}

op_ldap_error_def = {
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

op_error_def = {
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
    }
}


op_ldap_error = {
    'description': 'LDAP error',
    'schema': {
        '$ref': '#/definitions/LDAPError'
    },
}

op_error = {
    'description': 'Operational error',
    'schema': {
        '$ref': '#/definitions/OperationError'
    },
}

op_success = {
    'description': 'Operation result',
    'schema': {
        '$ref': '#/definitions/ResponseSuccess'
    },
}

# -*- coding: utf-8 -*-

param_include_nested = {
    'name': 'include_nested',
    'in': 'query',
    'type': 'boolean',
    'default': False,
    'required': False
}

param_filter = {
    'name': 'filter',
    'in': 'query',
    'type': 'string',
    'required': False
}


class Spec(object):
    parameters = []
    extra_definitions = {}

    def __init__(self, summary, tags):
        self.summary = summary
        self.tags = [tags]
        self.definitions = {
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
        self.responses = {
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

        if self.extra_definitions:
            self.definitions.update(self.extra_definitions)

    @classmethod
    def add_parameter(cls, param):
        cls.parameters.append(param)

    @staticmethod
    def get_path_parameter(name, data_type='string', required=True):
        return {
            'name': name,
            'in': 'path',
            'type': data_type,
            'required': required,
        }

    @classmethod
    def fields_from_schema(cls, config):
        fields = {
            'required': config['required_fields'],
            'properties': {}
        }

        for name, field in config['fields'].items():
            fields['properties'][name] = {
                'type': field['type'],
            }

        return fields

    def create(self):
        pass

    def delete(self):
        pass

    def many(self):
        pass

    def one(self):
        pass

    def update(self):
        pass

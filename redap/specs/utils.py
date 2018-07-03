# -*- coding: utf-8 -*-


def get_query_param(name, data_type='string', default=None, required=False):
    query_param = {
        'name': name,
        'in': 'query',
        'type': data_type,
        'required': required
    }

    if default is not None:
        query_param['default'] = default

    return query_param


def get_path_param(name, required=True):
    return {
        'name': name,
        'in': 'path',
        'type': 'string',
        'required': required,
    }


def get_body_param(ref, required=True):
    return {
        'type': 'object',
        'name': 'body',
        'required': required,
        'in': 'body',
        'schema': {
            '$ref': '#/definitions/{0}'.format(ref)
        },
    }


def get_response_body(code, definition):
    return {
        code: {
            'description': 'Operation response',
            'schema': definition
        }
    }


def def_from_schema(def_name, schema, many=False):
    fields = {
        'required': schema['required_fields'],
        'properties': {},
        'object': 'array' if many else 'object'
    }

    for name, field in schema['fields'].items():
        fields['properties'][name] = {
            'type': field['type'],
        }

    return {def_name: fields}

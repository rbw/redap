def get_query_param(name, data_type='string', default=None, required=False):
    query_param = {
        'name': name,
        'in': 'query',
        'type': data_type,
        'required': required
    }

    if default:
        query_param['default'] = default

    return query_param


def get_path_param(name, required=True):
    return {
        'name': name,
        'in': 'path',
        'type': 'string',
        'required': required,
    }


def get_body_param(definition, required=True):
    return {
        'type': 'object',
        'name': 'body',
        'required': required,
        'in': 'body',
        'schema': {
            '$ref': '#/definitions/{0}'.format(definition)
        },
    }


def spec_from_schema(schema):
    fields = {
        'required': schema['required_fields'],
        'properties': {},
        'type': 'object'
    }

    for name, field in schema['fields'].items():
        fields['properties'][name] = {
            'type': field['type'],
        }

    return fields

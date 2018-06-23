# -*- coding: utf-8 -*-

from functools import wraps
from furl import furl
from flasgger import swag_from, validate
from flask import request, jsonify, current_app as app
from lapdance.models.apikey import APIKey
from lapdance.exceptions import LapdanceError


def generate_apikey_table(api_keys):
    table = list()
    table.append('\nAPI key{0}Description'.format(' ' * 58))
    table.append('{0} {1}'.format('=' * 64, '=' * 16))

    for api_key in api_keys:
        enabled = '' if api_key.enabled else '*'
        table.append('{0}{1} {2}'.format(api_key.key, enabled, api_key.description))

    return '\n'.join(table)


def generate_spec_def(schema_name, config):
    fields = {
        'required': [],
        'properties': {}
    }

    for name, field in config['fields'].items():
        fields['properties'][name] = {
            'type': field['type'],
        }

        if field.get('required'):
            fields['required'].append(name)

    return {
        schema_name: fields
    }


def props_to_str(entry, **kwargs):
    """Converts value array to string if count <= 1, skips hidden fields"""

    formatted = {}
    skip_fields = kwargs.pop('skip_fields', [])

    for field_name, value in entry.get_attributes_dict().items():
        if field_name in skip_fields:
            continue

        if len(value) == 1:
            formatted[field_name] = value[0]
        elif len(value) < 1:
            formatted[field_name] = None
        else:
            formatted[field_name] = value

    return formatted


def validation_error(*args):
    raise LapdanceError(message=args[0].message, status_code=422)


def route(bp, *args, **kwargs):
    method = kwargs.pop('method', 'GET').upper()
    status = 201 if method == 'POST' else 200

    kwargs['strict_slashes'] = kwargs.pop('strict_slashes', False)
    kwargs['methods'] = [method]
    spec = kwargs.pop('spec')

    def decorator(f):
        @bp.route(*args, **kwargs)
        @swag_from(spec)
        @wraps(f)
        def wrapper(*inner_args, **inner_kwargs):
            api_key = request.headers.get('x-api-key')
            if app.config['AUTH_TYPE'] == 'api_key':
                if not APIKey.get_one(api_key):
                    if api_key:
                        app.logger.info('Invalid authorization with API key: {0}...'.format(api_key[0:24]))
                    else:
                        app.logger.info('No API key was provided')

                    raise LapdanceError(message='Unauthorized', status_code=401)

            if method == 'GET':  # Inject _params
                url = furl(request.url)
                inner_kwargs['_params'] = dict(url.query.params)
            elif method in ['POST', 'PUT']:
                # Inject validated parameters on insert / update operations (if a body is expected)
                print(spec)
                if any(p for p in spec['parameters'] if p['name'] == 'body' and p['required']):
                    if method == 'POST':
                        validate(request.get_json(), specs=spec, validation_error_handler=validation_error)

                    inner_kwargs['_payload'] = request.get_json()

            response = f(*inner_args, **inner_kwargs)
            if isinstance(response, str):
                app.logger.info(response)
                response = {'result': response}

            return jsonify(response), status

        return f

    return decorator


# -*- coding: utf-8 -*-

from functools import wraps
from furl import furl
from flasgger import swag_from
from flask import request, jsonify, current_app as app
from lapdance.models.apikey import APIKey
from lapdance.exceptions import LapdanceError
from sqlalchemy.orm.exc import NoResultFound


def generate_apikey_table(api_keys):
    table = list()
    table.append('\nAPI key{0}Description'.format(' ' * 58))
    table.append('{0} {1}'.format('=' * 64, '=' * 16))

    for api_key in api_keys:
        enabled = '' if api_key.enabled else '*'
        table.append('{0}{1} {2}'.format(api_key.key, enabled, api_key.description))

    return '\n'.join(table)


def generate_spec_def(name, config, required_fields=False):
    return {
        name: {
            'required': config['required_fields'] if not required_fields else [],
            'properties': {k: {'type': v['type']} for k, v in config['fields'].items()}
        }
    }


def build_dn(rdn, base_dn):
    return rdn and "{0},{1}".format(rdn, base_dn) or base_dn


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
                params = furl(request.url).args
                inner_kwargs['_params'] = dict(params)
            elif method in ['POST', 'PUT']:  # Inject payload on insert / update operations
                inner_kwargs['_payload'] = request.get_json()

            response = f(*inner_args, **inner_kwargs)
            if isinstance(response, str):
                app.logger.info(response)
                response = {'result': response}

            return jsonify(response), status

        return f

    return decorator


# -*- coding: utf-8 -*-

from functools import wraps
from furl import furl
from flasgger import swag_from, validate
from flask import request, jsonify, current_app as app
from redap.models.apikey import APIKey
from redap.exceptions import RedapError


def validation_error(*args):
    raise RedapError(message=args[0].message, status_code=422)


def route(bp, *args, **kwargs):
    method = kwargs.pop('method', 'GET').upper()
    status = 201 if method == 'POST' else 200

    kwargs['strict_slashes'] = kwargs.pop('strict_slashes', False)
    kwargs['methods'] = [method]
    spec = kwargs.pop('spec')
    print(spec.__dict__)

    def decorator(f):
        @bp.route(*args, **kwargs)
        @swag_from(spec.__dict__)
        @wraps(f)
        def wrapper(*inner_args, **inner_kwargs):
            api_key = request.headers.get('x-api-key')
            if app.config['AUTH_TYPE'] == 'api_key':
                if not APIKey.get_one(api_key):
                    if api_key:
                        app.logger.info('Invalid authorization with API key: {0}...'.format(api_key[0:24]))
                    else:
                        app.logger.info('No API key was provided')

                    raise RedapError(message='Unauthorized', status_code=401)

            if method == 'GET':  # Inject _params
                url = furl(request.url)
                inner_kwargs['_params'] = dict(url.query.params)
            elif method in ['POST', 'PUT']:
                # Inject validated parameters on insert / update operations (if a body is expected)
                if any(p for p in spec.parameters if p['name'] == 'body' and p['required']):
                    if method == 'POST':
                        validate(request.get_json(), specs=spec.__dict__, validation_error_handler=validation_error)

                    inner_kwargs['_payload'] = request.get_json()

            response = f(*inner_args, **inner_kwargs)
            if isinstance(response, str):
                app.logger.info(response)
                response = {'result': response}

            return jsonify(response), status

        return f

    return decorator


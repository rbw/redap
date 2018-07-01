# -*- coding: utf-8 -*-

from flask import jsonify, request
from flask_graphql import GraphQLView
import traceback
from redap import factory
from redap.core import cors, swagger
from redap.settings import user_schema
from redap.exceptions import RedapError
from ldap3.core.exceptions import LDAPException, LDAPOperationResult
from .users import bp as users_bp
from .groups import bp as groups_bp


def log_traceback(app, exception):
    tb = traceback.format_tb(exception.__traceback__)
    app.logger.debug(''.join(tb))


def register_blueprints(app, blueprints):
    for bp in blueprints:
        app.register_blueprint(bp, url_prefix='/{0}/{1}'.format('api', bp.name))


def create_app(*args, **kwargs):
    app = factory.create_app(__name__, *args, **kwargs)
    cors.init_app(app)

    # Attach bundles
    register_blueprints(app, [users_bp, groups_bp])

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=user_schema.graphene_schema,
            graphiql=True
        )
    )

    # Init swagger and inject model props
    swagger.init_app(app)

    @app.errorhandler(LDAPException)
    def handle_ldap_error(error):
        status = 400

        if isinstance(error, LDAPOperationResult):
            errmsg = error.__dict__
            [errmsg.pop(k) for k in ['dn', 'response']]
        else:

            status = 500
            errmsg = "LDAP error: {0}".format(error)

        if app.config['DEBUG']:
            log_traceback(app, error)

        app.logger.error(errmsg)

        response = errmsg if app.config.get('REDAP_SHOW_LDAP_ERROR_DETAILS') else 'Error performing LDAP operation'
        return jsonify(code=status, message=response), status

    @app.errorhandler(RedapError)
    def handle_invalid_usage(error):
        msg = "{0} (path: {1}, method: {2})".format(error.message, request.path, request.method)

        if app.config['DEBUG']:
            log_traceback(app, error)

        if str(error.status_code)[0] == '4':  # Log info on HTTP 4xx
            app.logger.info(msg)
        else:
            app.logger.warning(msg)

        return jsonify(error.to_dict()), error.status_code

    return app

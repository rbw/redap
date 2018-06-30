# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask.logging import default_handler
from redap.core import ldap, db, migrate
from redap.models import LDAPUser, LDAPGroup


def create_app(package_name, *args, **kwargs):
    app = Flask(package_name, *args, instance_relative_config=True, **kwargs)

    # Fetch settings from config file
    app.config.from_object('redap.settings')

    # Init flask-ldapconn extension
    ldap.init_app(app)

    # Init SQLAlchemy
    db.init_app(app)
    migrate.init_app(app, db)

    # LDAP config
    base_dn = app.config.get('REDAP_BASE_DN')
    user_config = app.config['REDAP_LDAP_USER']
    group_config = app.config['REDAP_LDAP_GROUP']

    user_fields = user_config['fields']
    group_fields = group_config['fields']

    # Init LDAP user model
    LDAPUser.init_model(
        object_classes=user_config['classes'],
        base_dn=base_dn,
        entry_rdn=[user_fields['id']['ref']],
        fields=user_fields
    )

    # Init LDAP group model
    LDAPGroup.init_model(
        object_classes=group_config['classes'],
        base_dn=base_dn,
        entry_rdn=group_fields['id']['ref'],
        fields=group_fields,
    )

    if app.config['ENV'] == 'production':
        formatter = logging.Formatter(app.config['LOG_FORMAT'])

        handler = RotatingFileHandler('logs/application.log', maxBytes=10000, backupCount=3)
        handler.setLevel(logging.INFO)
        handler.setFormatter(formatter)

        app.logger.setLevel(logging.INFO)
        app.logger.addHandler(handler)
        app.logger.removeHandler(default_handler)

    # Check for errors upon request teardown
    @app.teardown_request
    def log_errors(error):
        if error is None:
            return

        app.logger.error("An error occurred while handling the request", error)

    return app

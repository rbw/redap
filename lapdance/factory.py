# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask.logging import default_handler
from lapdance.core import ldap, db, migrate
from lapdance.utils import build_dn
from lapdance.models import LDAPUser, LDAPGroup


def create_app(package_name, *args, **kwargs):
    app = Flask(package_name, *args, instance_relative_config=True, **kwargs)

    # Fetch settings from config file
    app.config.from_object('lapdance.settings')

    # Init flask-ldapconn extension
    ldap.init_app(app)

    # Init SQLAlchemy
    db.init_app(app)
    migrate.init_app(app, db)

    # LDAP config
    base_dn = app.config.get('LAPDANCE_BASE_DN')
    user_config = app.config['LAPDANCE_LDAP_USER']
    group_config = app.config['LAPDANCE_LDAP_GROUP']

    # Init LDAP user model
    LDAPUser.init_model(
        object_classes=user_config['classes'],
        base_dn=build_dn(user_config.get('relative_dn'), base_dn),
        fields=user_config['fields']
    )

    # Init LDAP group model
    LDAPGroup.init_model(
        object_classes=group_config['classes'],
        base_dn=build_dn(group_config.get('relative_dn'), base_dn),
        fields=group_config['fields'],
    )

    if app.config['ENV'] != 'devel':
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

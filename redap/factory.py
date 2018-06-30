# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask.logging import default_handler
from redap.core import ldap, db, migrate


def create_app(package_name, *args, **kwargs):
    app = Flask(package_name, *args, instance_relative_config=True, **kwargs)

    # Fetch settings from config file
    app.config.from_object('redap.settings.core')
    app.config.from_object('redap.settings.ldap')

    # Init flask-ldapconn extension
    ldap.init_app(app)

    # Init SQLAlchemy
    db.init_app(app)
    migrate.init_app(app, db)

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

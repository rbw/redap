# -*- coding: utf-8 -*-

import os
from unittest import TestCase
from redap.api import create_app


class FlaskTestCase(TestCase):
    """Mix-in class for creating the Flask application."""

    def setUp(self):
        os.environ['ENV'] = 'testing'
        app = create_app()
        app.logger.disabled = True
        self.app = app

    def tearDown(self):
        self.app = None

    def tes(self):
        self.assertEqual(self.app.config['REDAP_LDAP_USER']['relative_dn'], True)

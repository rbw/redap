# -*- coding: utf-8 -*-

from lapdance.core import ldap


class LDAPCollection(ldap.Model):
    """Class for dynamically creating an LDAP model using arbitrary fields from the configuration

    :param name: Class name
    """

    def __init__(self, name):
        self.model = None
        self.mappings = []
        self.name = name

    def __call__(self, *args, **kwargs):
        return self.model

    def init_model(self, **kwargs):
        """Takes various configuration parameters and generates an ldap.Entry and assigns to self.model.

        :param kwargs: Model properties
        """

        attributes = {k: ldap.Attribute(v['ldap_name']) for k, v in kwargs.pop('fields').items()}
        attributes.update(**kwargs)

        # Create new instance of ldap.Entry using `type` and have it registered.
        self.model = globals()[self.name] = type(self.name, (ldap.Entry, ), attributes)

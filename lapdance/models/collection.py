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

    def init_model(self, object_classes, base_dn, fields):
        """Takes various configuration parameters and generates an ldap.Entry and assigns to self.model.

        :param object_classes: List of LDAP objectClasses (e.g. top, user, person)
        :param base_dn: Base DN of this collection
        :param fields: List of LDAP field mappings
        """

        attributes = {k: ldap.Attribute(v['ldap_name']) for k, v in fields.items()}
        attributes.update({
            'base_dn': base_dn,
            'entry_rdn': fields.get('name'),
            'object_classes': object_classes,
        })

        # Create new instance of ldap.Entry using `type` and have it registered.
        self.model = globals()[self.name] = type(self.name, (ldap.Entry,), attributes)

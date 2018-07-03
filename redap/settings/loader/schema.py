# -*- coding: utf-8 -*-

import os
from redap.settings.schemas import container_schema, default_profiles
from redap.core import ldap
from .base import Loader


class SchemaLoader(Loader):
    def __init__(self, file_name, base_dn, dirtype, **kwargs):
        self.entry_name = os.path.splitext(file_name)[0]
        self.base_dn = base_dn
        self.dirtype = dirtype
        self.file_name = file_name

        if self.dirtype in default_profiles:
            data = self._open(file_name)
            profile = default_profiles[self.dirtype].get(self.entry_name)
            kwargs.update(
                {
                    'data': self._populate_defaults(data, profile)
                }
            )

        super(SchemaLoader, self).__init__(file_name, schema=container_schema, **kwargs)

    @staticmethod
    def _populate_defaults(data, defaults):
        def _is_empty(value):
            if (
                isinstance(value, str) and not value
                or
                isinstance(value, list) and len(value) == 0
            ):
                return True

            return False

        for k, v in defaults.items():
            # Set value from profile if empty
            if k not in data or _is_empty(data[k]):
                data[k] = v

        return data

    def _get_cls_name(self, prefix):
        return "{0}{1}".format(prefix, self.entry_name.capitalize())

    @property
    def fields(self):
        return self.data['fields']

    @property
    def ldap_model(self):
        attributes = {k: ldap.Attribute(v['ref']) for k, v in self.fields.items()}
        attributes.update({
            'object_classes': self.data['classes'],
            'base_dn': self.base_dn,
            'entry_rdn': self.fields['id']['ref'],
        })

        name = self._get_cls_name('LDAP')
        cls = globals()[name] = type(name, (ldap.Entry, ), attributes)
        return cls

# -*- coding: utf-8 -*-

from flask import current_app as app
from ldap3 import MODIFY_REPLACE
from lapdance.core import ldap
from lapdance.exceptions import LapdanceError
from lapdance.utils import props_to_str


class ResponseHandler(object):
    def __init__(self, response, config, raise_on_empty=False):
        self.entries = response.all()
        self.config = config
        self.count = len(self.entries)

        if self.count == 0 and raise_on_empty:
            raise LapdanceError(message='No such object', status_code=404)

    def result(self, as_dict=False):
        if as_dict:
            return [props_to_str(e, skip_fields=self.config['hidden_fields']) for e in self.entries]

        return self.entries


class Service(object):
    __model__ = None
    __config_name__ = None

    @property
    def conn(self):
        return ldap.connection

    @property
    def model(self):
        """Returns instance of the associated model class"""

        return self.__model__()

    @property
    def config(self):
        return app.config[self.__config_name__]

    @property
    def fields(self):
        return self.config['fields']

    @property
    def dirtype(self):
        return app.config['LAPDANCE_LDAP_DIRTYPE']

    @property
    def _microsoft_ext(self):
        self._raise_if_incompatible_with('ad')
        return self.conn.extend.microsoft

    def _raise_if_incompatible_with(self, dirtype):
        if dirtype != self.dirtype:
            raise LapdanceError(message='Operation not compatible with this directory server', status_code=500)

    def _get_matching(self, query_filter=None, raise_on_empty=False):
        return ResponseHandler(
            self.model.query.filter(query_filter),
            self.config,
            raise_on_empty=raise_on_empty
        )

    def _get_entry_dn(self, id_value):
        return "{0}={1},{2},{3}".format(self.fields['id']['ldap_name'],
                                        id_value,
                                        self.config['relative_dn'],
                                        self.model.base_dn)

    def _create_payload(self, params, operation=None):
        """Create LDAP payload from dict"""

        payload = {}

        for name, field in self.fields.items():
            # Look for missing props if operation is None (add) and set defaults.
            # No need to check for constraints as the input has been validated already.
            if name not in params:
                if 'default' in field and operation is None:
                    value = field['default']
                else:
                    continue
            else:
                value = params[name]

            if operation:
                value = [(operation, value, )]

            payload[field['ldap_name']] = value

        return payload

    def _modify(self, id_value, params):
        self.conn.modify(dn=self._get_entry_dn(id_value),
                         changes=self._create_payload(params, MODIFY_REPLACE))

    def _add(self, params):
        self.conn.add(dn=self._get_entry_dn(params['id']),
                      object_class=self.config['classes'],
                      attributes=self._create_payload(params))

    def get_many(self, **kwargs):
        as_dict = kwargs.pop('as_dict', True)
        return self._get_matching(
            query_filter=kwargs.pop('filter', ''),
            **kwargs,
        ).result(as_dict=as_dict) or []

    def get_one(self, id_value, raise_on_empty=True, as_dict=False):
        id_field = self.config['fields']['id']
        return self._get_matching(
            query_filter='({0}={1})'.format(id_field['ldap_name'], id_value),
            raise_on_empty=raise_on_empty,
        ).result(as_dict=as_dict)[0]

    def update(self, id_value, params):
        self._modify(id_value, params)

    def create(self, params):
        self._add(params)

    def delete(self, query_id):
        self.conn.delete(self._get_entry_dn(query_id))

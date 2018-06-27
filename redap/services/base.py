# -*- coding: utf-8 -*-

from flask import current_app as app
from ldap3 import MODIFY_REPLACE
from redap.core import ldap
from redap.exceptions import RedapError
from redap.utils import props_to_str

ACTIVE_DIRECTORY = 'ad'
FREEIPA = 'freeipa'

ADD = 'ADD'
REPLACE = MODIFY_REPLACE


class ResponseHandler(object):
    def __init__(self, response, config, raise_on_empty=False):
        self.entries = response.all()
        self.config = config
        self.count = len(self.entries)

        if self.count == 0 and raise_on_empty:
            raise RedapError(message='No such object', status_code=404)

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
    def is_secure(self):
        return self.config['LDAP_USE_SSL']

    @property
    def model(self):
        return self.__model__()

    @property
    def config(self):
        return app.config[self.__config_name__]

    @property
    def fields(self):
        return self.config['fields']

    @property
    def dirtype(self):
        return app.config['REDAP_LDAP_DIRTYPE']

    @property
    def _microsoft_ext(self):
        self._raise_if_incompatible_with(ACTIVE_DIRECTORY)
        return self.conn.extend.microsoft

    def _raise_if_incompatible_with(self, dirtype):
        if dirtype != self.dirtype:
            raise RedapError(message='Operation not compatible with this directory server', status_code=500)

    def _get_matching(self, query_filter=None, raise_on_empty=False):
        return ResponseHandler(
            self.model.query.filter(query_filter),
            self.config,
            raise_on_empty=raise_on_empty
        )

    def get_field_by_ref(self, ref_name):
        return next((n for n, f in self.fields.items() if f['ref'] == ref_name), None)

    def _get_entry_dn(self, id_value, params):
        if self.dirtype == ACTIVE_DIRECTORY:
            cn_key = self.get_field_by_ref('cn')
            if cn_key is None:
                raise RedapError(message="Missing 'cn' ref field, cannot continue", status_code=500)

            rdn = 'cn={0}'.format(params[cn_key])
        else:
            rdn = '{0}={1}'.format(self.fields['id']['ref'], id_value)

        return '{0},{1},{2}'.format(rdn, self.config['relative_dn'], self.model.base_dn)

    def _create_payload(self, params, operation):
        payload = {}

        for name, field in self.fields.items():
            # Look for missing props if operation is None (add) and set defaults.
            # No need to check for constraints as the input has been validated already.
            if name not in params:
                if 'default' in field and operation == ADD:
                    value = field['default']
                else:
                    continue
            else:
                value = params[name]

            if operation == REPLACE:
                value = [(operation, value, )]

            payload[field['ref']] = value

        return payload

    def _modify(self, id_value, params, operation=REPLACE):
        self.conn.modify(dn=self.get_one(id_value).dn,
                         changes=self._create_payload(params, operation))

    def _add(self, params):
        self.conn.add(dn=self._get_entry_dn(params['id'], params),
                      object_class=self.config['classes'],
                      attributes=self._create_payload(params, ADD))

    def get_many(self, as_dict=True, **kwargs):
        return self._get_matching(
            query_filter=kwargs.pop('filter', ''),
            **kwargs,
        ).result(as_dict=as_dict) or []

    def get_one(self, id_value, as_dict=False):
        id_field = self.config['fields']['id']
        return self._get_matching(
            query_filter='({0}={1})'.format(id_field['ref'], id_value),
            raise_on_empty=True,
        ).result(as_dict=as_dict)[0]

    def update(self, id_value, params):
        self._modify(id_value, params)

    def create(self, params):
        self._add(params)

    def delete(self, id_value):
        self.conn.delete(self.get_one(id_value).dn)

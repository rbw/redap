# -*- coding: utf-8 -*-

from flask import current_app as app
from ldap3 import MODIFY_REPLACE
from redap.core import ldap
from redap.exceptions import RedapError

ACTIVE_DIRECTORY = 'ad'
FREEIPA = 'freeipa'

ADD = 'ADD'
REPLACE = MODIFY_REPLACE


class ResponseHandler(object):
    def __init__(self, response, hidden_fields, raise_on_empty=False):
        self.entries = response.all()
        self.hidden_fields = hidden_fields
        self.count = len(self.entries)

        if self.count == 0 and raise_on_empty:
            raise RedapError(message='No such object', status_code=404)

    def props_to_str(self, entry):
        """Converts value array to string if count <= 1, skips hidden fields"""

        formatted = {}

        for field_name, value in entry.get_attributes_dict().items():
            if field_name in self.hidden_fields:
                continue

            if len(value) == 1:
                formatted[field_name] = value[0]
            elif len(value) < 1:
                formatted[field_name] = None
            else:
                formatted[field_name] = value

        return formatted

    def result(self, as_dict=False):
        if as_dict:
            return [self.props_to_str(e) for e in self.entries]

        return self.entries


class Service(object):
    __model__ = None
    __config__ = {}

    @property
    def conn(self):
        return ldap.connection

    @property
    def relative_dn(self):
        return self.__config__['relative_dn']

    @property
    def id_ref(self):
        return self.fields['id']['ref']

    @property
    def fields(self):
        return self.__config__['fields']

    @property
    def hidden_fields(self):
        return self.__config__['hidden_fields']

    @property
    def classes(self):
        return self.__config__['classes']

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

    def _get_matching(self, query_filter=None, **kwargs):
        return ResponseHandler(
            self.__model__.query.filter(query_filter),
            self.hidden_fields,
            **kwargs
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
            rdn = '{0}={1}'.format(self.id_ref, id_value)

        return '{0},{1},{2}'.format(rdn, self.relative_dn, self.__model__.base_dn)

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
                      object_class=self.classes,
                      attributes=self._create_payload(params, ADD))

    def get_many(self, **kwargs):
        return self._get_matching(
            query_filter=kwargs.pop('filter', ''),
            raise_on_empty=kwargs.pop('raise_on_empty', False)
        ).result(kwargs.pop('as_dict', True)) or []

    def get_one(self, id_value, **kwargs):
        return self._get_matching(
            query_filter='({0}={1})'.format(self.id_ref, id_value),
            raise_on_empty=kwargs.pop('raise_on_empty', True),
        ).result(kwargs.pop('as_dict', False))[0]

    def update(self, id_value, params):
        self._modify(id_value, params)

    def create(self, params):
        self._add(params)

    def delete(self, id_value):
        self.conn.delete(self.get_one(id_value).dn)

# -*- coding: utf-8 -*-

from flask import current_app as app
from lapdance.core import ldap
from lapdance.exceptions import LapdanceError

VENDOR_MICROSOFT = 'MICRO$OFT'
VENDOR_UNKNOWN = 'UNKNOWN'


class ResponseHandler(object):
    def __init__(self, response, config, raise_on_empty=False):
        self.entries = response.all()
        self.config = config
        self.count = len(self.entries)

        if self.count == 0 and raise_on_empty:
            raise LapdanceError(message='No such object', status_code=404)

    def props_to_str(self, entry):
        """Converts value array to string if count <= 1, skips hidden fields"""

        formatted = {}

        for field_name, value in entry.get_attributes_dict().items():
            if field_name in self.config['hidden_fields']:
                continue

            if len(value) > 1:
                formatted[field_name] = value
            else:
                formatted[field_name] = value[0]

        return formatted

    def result(self, as_dict=False):
        if as_dict:
            return [self.props_to_str(e) for e in self.entries]

        if self.count == 0:
            return []
        elif self.count == 1:
            return self.entries[0]

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
    def vendor_name(self):
        if 'forestFunctionality' in self.conn.server.info.other:
            return VENDOR_MICROSOFT

        return VENDOR_UNKNOWN

    @property
    def _microsoft_ext(self):
        self._raise_if_incompatible_with(VENDOR_MICROSOFT)
        return self.conn.extend.microsoft

    def _raise_if_incompatible_with(self, vendor):
        if vendor != self.vendor_name:
            raise LapdanceError(message='Operation not available for this directory server', status_code=500)

    def _get_matching(self, query_filter=None, raise_on_empty=False):
        """Perform LDAP query

        :param query_filter: Query filter string
        :param raise_on_empty: Raise exception if no records returned
        :return: ResponseHandler object
        """

        return ResponseHandler(
            self.model.query.filter(query_filter),
            self.config,
            raise_on_empty=raise_on_empty
        )

    def get_many(self, params=None, **kwargs):
        """Returns a list of entries matching the query params"""

        as_dict = kwargs.pop('as_dict', True)
        return self._get_matching(
            query_filter=params.pop('filter', ''),
            **kwargs,
        ).result(as_dict=as_dict)

    def get_one(self, id_value, raise_on_empty=True, as_dict=False):
        """Returns a single entry"""

        id_field = self.config['fields']['id']
        return self._get_matching(
            query_filter='({0}={1})'.format(id_field['ldap_name'], id_value),
            raise_on_empty=raise_on_empty,
        ).result(as_dict=as_dict)[0]

    def update(self, id_value, payload):
        """Updates an entry"""

        obj = self.get_one(id_value)
        for (k, v) in payload.items():
            setattr(obj, k, v)

        obj.save()

    def create(self, payload):
        self.model(**payload).save()

    def delete(self, query_id):
        obj = self.get_one(query_id)
        self.conn.delete(obj.dn)

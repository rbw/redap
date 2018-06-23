# -*- coding: utf-8 -*-

from flask import current_app as app
from lapdance.core import ldap
from lapdance.exceptions import LapdanceError
from lapdance.utils import props_to_str

VENDOR_MICROSOFT = 'MICRO$OFT'
VENDOR_UNKNOWN = 'UNKNOWN'


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

    def get_many(self, **kwargs):
        """Returns a list of entries matching the query params"""

        as_dict = kwargs.pop('as_dict', True)
        return self._get_matching(
            query_filter=kwargs.pop('filter', ''),
            **kwargs,
        ).result(as_dict=as_dict) or []

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
        fields = self.config['fields']

        self.conn.add(dn="{0}={1},{2}".format(fields['id']['ldap_name'], payload['id'], self.model.base_dn),
                      object_class=self.config['classes'],
                      attributes={fields[k]['ldap_name']: v for k, v in payload.items()})

    def delete(self, query_id):
        obj = self.get_one(query_id)
        self.conn.delete(obj.dn)

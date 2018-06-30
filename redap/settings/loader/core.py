# -*- coding: utf-8 -*-

from .base import Loader
from redap.settings.schemas import core_schema


class CoreLoader(Loader):
    def __init__(self, file_name='core.yml', **kwargs):
        super(CoreLoader, self).__init__(file_name, schema=core_schema, **kwargs)

# -*- coding: utf-8 -*-

from .base import Loader
from redap.settings.schemas import core_schema


class CoreLoader(Loader):
    def __init__(self, *args, **kwargs):
        super(CoreLoader, self).__init__(*args, schema=core_schema, **kwargs)

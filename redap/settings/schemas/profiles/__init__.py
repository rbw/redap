# -*- coding: utf-8 -*-

from .freeipa import defaults_freeipa
from .ad import defaults_ad


defaults = {
    'freeipa': defaults_freeipa,
    'ad': defaults_ad,
    'unknown': {
        'user.yml': {},
        'group.yml': {}
    }
}


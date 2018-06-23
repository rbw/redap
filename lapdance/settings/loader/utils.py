# -*- coding: utf-8 -*-

import yaml
import json
from cerberus import Validator
from lapdance.exceptions import InvalidConfiguration


def load_doc(file, schema=None, defaults=None):
    with open(file, 'r') as stream:
        try:
            doc = yaml.load(stream) or {}

            if defaults:
                # Apply defaults for the selected profile
                doc = _apply_directory_defaults(doc or {}, defaults)

            v = Validator(schema)
            v.allow_unknown = True
            v.validate(doc, schema)
            if v.errors:
                raise InvalidConfiguration(file, json.dumps(v.errors, indent=4, separators=(',', ': ')))

            return v.__dict__['document']
        except yaml.YAMLError as exception:
            raise exception


def _apply_directory_defaults(settings, defaults):
    def _is_empty(value):
        if isinstance(value, str) and not value:
            return True
        elif isinstance(value, list) and len(value) == 0:
            return True

        return False

    for k, v in defaults.items():
        # Set value from profile if empty
        if k not in settings or _is_empty(settings[k]):
            settings[k] = v

    return settings

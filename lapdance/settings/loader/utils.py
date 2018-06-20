# -*- coding: utf-8 -*-

import yaml
import json
from cerberus import Validator
from lapdance.exceptions import InvalidConfiguration


def load_doc(file, schema=None):
    with open(file, 'r') as stream:
        try:
            doc = yaml.load(stream)
            v = Validator(schema)
            v.allow_unknown = True
            v.validate(doc, schema)
            if v.errors:
                raise InvalidConfiguration(file, json.dumps(v.errors, indent=4, separators=(',', ': ')))

            return v.__dict__['document']
        except yaml.YAMLError as exception:
            raise exception


# -*- coding: utf-8 -*-

from redap.specs.definitions import ERROR_RESPONSES, ERROR_DEFINITIONS


def get_spec(tag, summary=None, params=None, defs=None, responses=None):
    spec = {
        'summary': summary or '<Unknown>',
        'tags': [tag],
        'parameters': params or [],
        'definitions': {
            **ERROR_DEFINITIONS,
        },
        'responses': {
            **ERROR_RESPONSES
        }
    }

    if isinstance(defs, list):
        [spec['definitions'].update(d) for d in defs]

    if responses:
        for status, data in responses:
            spec['responses'].update({status: data['response']})
            spec['definitions'].update(data['definition'])

    return spec



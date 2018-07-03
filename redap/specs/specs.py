# -*- coding: utf-8 -*-

from copy import copy
from redap.settings import user_schema, group_schema
from .utils import spec_from_schema, get_path_param
from .definitions import BASE_DEFINITIONS, BASE_RESPONSES


class Spec(object):
    def __init__(self, summary, parameters, tag=None, definition=None):
        self.definitions = copy(BASE_DEFINITIONS)
        self.responses = copy(BASE_RESPONSES)
        self.tags = [tag]

        if isinstance(definition, dict):
            self.definitions.update(
                **definition
            )

        self.summary = summary
        self.parameters = parameters


class UserSpec(Spec):
    def __init__(self, *args, params=None, definition=None, **kwargs):
        kwargs['definition'] = definition or {'User': spec_from_schema(user_schema.data)}
        kwargs['parameters'] = params or get_path_param('user_id')
        super(UserSpec, self).__init__(*args, tag=kwargs.pop('tag', 'users'), **kwargs)


class GroupSpec(Spec):
    def __init__(self, *args, params=None, definition=None, **kwargs):
        kwargs['definition'] = definition or {'Group': spec_from_schema(group_schema.data)}
        kwargs['parameters'] = params or get_path_param('group_id')
        super(GroupSpec, self).__init__(*args, tag=kwargs.pop('tag', 'groups'), **kwargs)

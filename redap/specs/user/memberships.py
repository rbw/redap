# -*- coding: utf-8 -*-

from redap.specs.group.many import group_many
from redap.specs.user import tags, user_id_path
from redap.specs.descriptions import USER_MEMBERSHIPS
from redap.specs.definitions import include_nested_param
from copy import deepcopy

user_memberships = deepcopy(group_many)
user_memberships['tags'] = tags
user_memberships['parameters'] = [user_id_path, include_nested_param]
user_memberships['summary'] = USER_MEMBERSHIPS

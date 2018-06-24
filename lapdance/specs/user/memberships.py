# -*- coding: utf-8 -*-

from lapdance.specs.group.many import group_many
from lapdance.specs.user import tags, user_id_path
from lapdance.specs.constants import USER_MEMBERSHIPS
from lapdance.specs.common import include_nested_param
from copy import deepcopy

user_memberships = deepcopy(group_many)
user_memberships['tags'] = tags
user_memberships['parameters'] = [user_id_path, include_nested_param]
user_memberships['summary'] = USER_MEMBERSHIPS

# -*- coding: utf-8 -*-

from lapdance.specs.group.many import group_many
from lapdance.specs.user import tags, user_id_path
from lapdance.specs.constants import USER_MEMBERSHIPS
from copy import deepcopy

user_memberships = deepcopy(group_many)
user_memberships['tags'] = tags
user_memberships['parameters'].append(user_id_path)
user_memberships['summary'] = USER_MEMBERSHIPS

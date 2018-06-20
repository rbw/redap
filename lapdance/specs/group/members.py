# -*- coding: utf-8 -*-

from lapdance.specs.user.many import user_many
from lapdance.specs.group import tags, group_id_path
from lapdance.specs.constants import GROUP_MEMBERS
from copy import deepcopy

group_members = deepcopy(user_many)
group_members['tags'] = tags
group_members['parameters'].append(group_id_path)
group_members['summary'] = GROUP_MEMBERS

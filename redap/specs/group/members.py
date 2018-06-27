# -*- coding: utf-8 -*-

from redap.specs.user.many import user_many
from redap.specs.group import tags, group_id_path
from redap.specs.descriptions import GROUP_MEMBERS
from redap.specs.definitions import include_nested_param
from copy import deepcopy

group_members = deepcopy(user_many)
group_members['tags'] = tags
group_members['parameters'] = [group_id_path, include_nested_param]
group_members['summary'] = GROUP_MEMBERS

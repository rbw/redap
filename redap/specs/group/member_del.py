# -*- coding: utf-8 -*-

from redap.specs.group import ldap_operation_spec
from redap.specs.group import tags
from redap.specs.user import user_id_path
from redap.specs.descriptions import GROUP_MEMBER_DEL
from copy import deepcopy

group_member_del = deepcopy(ldap_operation_spec)
group_member_del['tags'] = tags
group_member_del['parameters'].append(user_id_path)
group_member_del['summary'] = GROUP_MEMBER_DEL

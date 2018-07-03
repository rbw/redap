# -*- coding: utf-8 -*-

from .specs import UserSpec, GroupSpec
from .definitions import MEMBER_ADD, CREDENTIALS, PASSWORD_CHANGE
from .utils import get_body_param, get_path_param, get_query_param

# ################# #
# User spec objects #
# ################# #
user_create = UserSpec('Create new user', params=[get_body_param('User')])
user_update = UserSpec('Update user', params=[get_path_param('user_id'), get_body_param('User')])
user_delete = UserSpec('Remove user')
user_one = UserSpec('Get single user')
user_many = UserSpec('Get list of users',
                     params=[
                         get_query_param('filter'),
                         get_query_param('include_nested', required=False)
                     ])

user_groups = GroupSpec('Get list of members',
                        tag='users',
                        params=[
                            get_path_param('user_id'),
                            get_path_param('group_id'),
                            get_query_param('include_nested', required=False)
                        ])

user_unlock = UserSpec('Unlocks the user account')
user_enable = UserSpec('Enable user account')
user_disable = UserSpec('Disable user account')
user_pw_never_expires = UserSpec('Sets password-never-expires for user')
user_pw_change = UserSpec('Set new password',
                          params=[get_path_param('user_id'), get_body_param('PasswordChange')],
                          definition=PASSWORD_CHANGE)

user_authenticate = UserSpec('Authenticate user',
                             params=[get_path_param('user_id'), get_body_param('Credentials')],
                             definition=CREDENTIALS)


# ################## #
# Group spec objects #
# ################## #
group_create = GroupSpec('Create new group', params=[get_body_param('Group')])
group_update = GroupSpec('Update group', params=[get_path_param('group_id'), get_body_param('Group')])
group_delete = GroupSpec('Remove group')
group_one = GroupSpec('Get single group')
group_many = GroupSpec('Get list of groups',
                       params=[
                           get_query_param('filter'),
                           get_query_param('include_nested', required=False)
                       ])

group_members = UserSpec('Get list of members',
                         tag='groups',
                         params=[
                             get_path_param('group_id'),
                             get_path_param('user_id'),
                             get_query_param('include_nested', required=False)
                         ])

group_member_add = GroupSpec('Add user to group',
                             params=[get_body_param('MemberAdd')],
                             definition=MEMBER_ADD)

group_member_del = GroupSpec('Remove user from group',
                             params=[
                                 get_path_param('group_id'),
                                 get_path_param('user_id')
                             ])

from pprint import pprint
pprint(group_members.__dict__)

# -*- coding: utf-8 -*-

from flask import Blueprint

from redap.services import groups
from redap.utils import route
from redap.specs import (
    group_one, group_many, group_create, group_delete,
    group_update, group_members, group_member_add, group_member_del,
)

bp = Blueprint('groups', __name__, url_prefix='/groups')


@route(bp, '/', spec=group_many)
def get_many(_params):
    return groups.get_many(**_params)


@route(bp, '/', method='POST', spec=group_create)
def create(_payload):
    groups.create(_payload)
    return 'Created group {0}'.format(_payload['id'])


@route(bp, '/<group_id>', method='DELETE', spec=group_delete)
def delete(group_id):
    groups.delete(group_id)
    return 'Deleted group {0}'.format(group_id)


@route(bp, '/<group_id>', spec=group_one)
def get_one(group_id, _params=None):
    return groups.get_one(group_id, as_dict=True)


@route(bp, '/<group_id>/members', spec=group_members)
def get_group_users(group_id, _params):
    return groups.get_members(group_id, **_params)


@route(bp, '/<group_id>/members', method='POST', spec=group_member_add)
def add_member(group_id, _payload):
    groups.add_member(group_id, _payload)
    return 'Added user {0} to group {1}'.format(_payload['id'], group_id)


@route(bp, '/<group_id>/members/<user_id>', method='DELETE', spec=group_member_del)
def remove_member(group_id, user_id):
    groups.remove_member(group_id, user_id)
    return 'Removed user {0} from group {1}'.format(user_id, group_id)


@route(bp, '/<group_id>', method='PUT', spec=group_update)
def update(group_id, _payload):
    groups.update(group_id, _payload)
    return 'Group {0} updated'.format(group_id)


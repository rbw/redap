# -*- coding: utf-8 -*-

from flask import Blueprint

from lapdance.services import users
from lapdance.utils import route
from lapdance.specs import (
    user_one, user_many, user_create, user_delete,
    user_update, user_memberships, user_password,
    user_unlock, user_enable, user_disable,
    user_pw_never_expires
)

bp = Blueprint('users', __name__, url_prefix='/users')


@route(bp, '/', spec=user_many)
def get_many(_params):
    return users.get_many(_params)


@route(bp, '/', method='POST', spec=user_create)
def create(_payload):
    users.create(_payload)
    return 'Created user {0}'.format(_payload['id'])


@route(bp, '/<user_id>', method='DELETE', spec=user_delete)
def delete(user_id):
    users.delete(user_id)
    return 'Deleted user {0}'.format(user_id)


@route(bp, '/<user_id>', spec=user_one)
def get_one(user_id, _params=None):
    return users.get_one(user_id, as_dict=True)


@route(bp, '/<user_id>/groups', spec=user_memberships)
def get_user_groups(user_id, _params):
    return users.get_groups(user_id, **_params)


@route(bp, '/<user_id>', method='PUT', spec=user_update)
def update(user_id, _payload):
    users.update(user_id, _payload)
    return 'User {0} updated'.format(user_id)


@route(bp, '/<user_id>/password', method='PUT', spec=user_password)
def set_password(user_id, _payload):
    users.set_password(user_id, _payload)
    return 'Password set for {0}'.format(user_id)


@route(bp, '/<user_id>/unlock', method='PUT', spec=user_unlock)
def unlock(user_id):
    users.unlock(user_id)
    return 'Unlocked user {0}'.format(user_id)


@route(bp, '/<user_id>/enable', method='PUT', spec=user_enable)
def enable(user_id):
    users.enable(user_id)
    return 'Enabled user {0}'.format(user_id)


@route(bp, '/<user_id>/disable', method='PUT', spec=user_disable)
def disable(user_id):
    users.disable(user_id)
    return 'Disabled user {0}'.format(user_id)


@route(bp, '/<user_id>/pw-never-expires', method='PUT', spec=user_pw_never_expires)
def set_pw_never_expires(user_id):
    users.pw_never_expires(user_id)
    return 'Password never expires set for user {0}'.format(user_id)

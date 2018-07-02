# -*- coding: utf-8 -*-

from redap.settings import user_schema
from .base import Spec


class User(Spec):
    description = None
    extra_definitions = {}
    params = [{
        'type': 'object',
        'name': 'body',
        'required': True,
        'in': 'body',
        'schema': {
            '$ref': '#/definitions/User'
        },
    }]

    def __init__(self):
        if not self.extra_definitions:
            self.extra_definitions.update(
                {
                    'User': self.fields_from_schema(user_schema.data)
                }
            )

        super(User, self).__init__(
            self.description,
            tags='users'
        )


class UserOperation(User):
    def __init__(self):
        params = self.get_path_parameter('user_id')
        if self.params:
            self.params.append(params)

        super(UserOperation, self).__init__()


class UserCreate(UserOperation):
    description = 'Create new user'


class UserUpdate(UserOperation):
    description = 'Update user'


class UserDelete(UserOperation):
    description = 'Remove user'


class UserMany(UserOperation):
    description = 'Get list of users'
    params = [
        {
            'name': 'filter',
            'in': 'query',
            'type': 'string',
            'required': False
        }
    ]


class UserOne(UserOperation):
    description = 'Get single user'


class UserPassword(UserOperation):
    description = 'Set new password'
    extra_definitions = {
        'PasswordChange': {
            'type': 'object',
            'required': ['new_password'],
            'properties': {
                'new_password': {
                    'type': 'string'
                },
                'old_password': {
                    'type': 'string'
                }
            }
        }
    }

    params = [
        {
            'type': 'object',
            'name': 'body',
            'required': True,
            'in': 'body',
            'schema': {
                '$ref': '#/definitions/PasswordChange'
            }
        }
    ]


class UserAuthenticate(UserOperation):
    description = 'Test user authentication'
    extra_definitions = {
        'Credentials': {
            'type': 'object',
            'required': ['username', 'password'],
            'properties': {
                'username': {
                    'type': 'string'
                },
                'password': {
                    'type': 'string'
                }
            }
        }
    }

    params = [{
        'type': 'object',
        'name': 'body',
        'required': True,
        'in': 'body',
        'schema': {
            '$ref': '#/definitions/Credentials'
        },
    }]


class UserPasswordNeverExpires(UserOperation):
    description = 'Sets password-never-expires for user'


class UserUnlock(UserOperation):
    description = 'Unlocks the user account'


class UserDisable(UserOperation):
    description = 'Disable user account'


class UserEnable(UserOperation):
    description = 'Enable user account'

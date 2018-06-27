# -*- coding: utf-8 -*-


class RedapError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return {
            'code': self.status_code,
            'message': self.message,
        }


class InvalidConfiguration(Exception):
    def __init__(self, file, cause):
        Exception.__init__(self)
        self.file = file
        self.cause = cause



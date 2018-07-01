# -*- coding: utf-8 -*-

from .base import Spec


class UserSpec(Spec):
    def authenticate(self):
        pass

    def disable(self):
        pass

    def enable(self):
        pass

    def memberships(self):
        pass

    def password(self):
        pass

    def pw_never_expires(self):
        pass

    def unlock(self):
        pass

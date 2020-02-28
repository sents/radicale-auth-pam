# -*- coding: utf-8 -*-
#
# This file is part of Radicale Server - Calendar Server
# Copyright © 2011 Corentin Le Bail
# Copyright © 2011-2013 Guillaume Ayoub
# Copyright © 2015 Raoul Thill
# Copyright © 2017 Marco Huenseler
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Radicale.  If not, see <http://www.gnu.org/licenses/>.

"""
LDAP authentication.
Authentication based on the ``ldap3`` module
(https://github.com/cannatag/ldap3/).
"""

from radicale.auth import BaseAuth
from pam import pam
import pwd


class Auth(BaseAuth):
    def __init__(self, configuration, logger):
        self.configuration = configuration
        self.logger = logger
        self.pam = pam()

    def is_authenticated(self, user, password):
        """Check if ``user``/``password`` couple is valid."""
        try:
            pwd.getpwnam(user)
        except KeyError:
            self.logger.debug("PAM No such user: {}".format(user))
            return False
        if self.pam.authenticate(user, password):
            self.logger.debug("PAM authenticated user {}".format(user))
            return True
        else:
            self.logger.debug("PAM invalid credentials for user {}".format(user))
            return False

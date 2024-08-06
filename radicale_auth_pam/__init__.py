import threading

from pam import pam
from radicale.auth import BaseAuth
from radicale.log import logger

class Auth(BaseAuth):
    def __init__(self, configuration):
        super().__init__(configuration)
        self.configuration = configuration
        if "pam_service" not in self.configuration.options("auth"):
            self.service = 'login'
        else:
            self.service = self.configuration.get("auth", "pam_service")
        self.local = threading.local()

    def login(self, user, password):
        """Check if ``user``/``password`` couple is valid."""
        if not hasattr(self.local, "pam_instance"):
            self.local.pam_instance = pam()
        if self.local.pam_instance.authenticate(user, password, self.service):
            logger.debug("PAM authenticated user {}".format(user))
            return user
        else:
            logger.debug("PAM could not authenticate user {}".format(user))
            return ""

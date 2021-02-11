from radicale.auth import BaseAuth
from pam import pam


class Auth(BaseAuth):
    def __init__(self, configuration, logger):
        self.configuration = configuration
        self.logger = logger
        self.service = self.configuration.get("auth", "pam_service", fallback="login")
        self.pam = pam()

    def is_authenticated(self, user, password):
        """Check if ``user``/``password`` couple is valid."""
        if self.pam.authenticate(user, password, self.service):
            self.logger.debug("PAM authenticated user {}".format(user))
            return True
        else:
            self.logger.debug("PAM could not authenticate user {}".format(user))
            return False

from logger import Logger

logger = Logger()

class CredentialInvalid(Exception):
    def __init__(self, msg=None):
        logger(instance=self, data=msg)
        return super().__init__(msg)

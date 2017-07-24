class Authenticator(object):

    def __init__(self, driver):
        self.driver = driver

    def authenticate(self):
        raise NotImplementedError

from selenium.common.exceptions import NoSuchElementException
from lmsa.authentication.Authenticator import Authenticator

class Duo(Authenticator):

    AUTH_XPATH = '//*[@id="login-form"]/fieldset[2]/div[1]/button'
    IFRAME = 'duo_iframe'

    def __switch_frame__(self):
        try:
            self.driver.switch_to_frame(Duo.IFRAME)
        except Exception as e:
            return False
        return True

    def __send_push__(self):
        self.driver.find_element_by_xpath(Duo.AUTH_XPATH).click()

    def authenticate(self):
        import time
        stall_title = self.driver.title
        try:
            if self.__switch_frame__():
                self.__send_push__()
                while stall_title == self.driver.title:
                    time.sleep(1)
            else:
                print('Error finding DUO iframe')
                time.sleep(1)

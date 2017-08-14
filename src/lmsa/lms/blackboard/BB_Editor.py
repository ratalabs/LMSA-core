"""
Handles any editing operations/logic unique to the Blackboard LMS
"""

from lmsa.lms.blackboard.options import assignment_options
from lmsa.lms.blackboard.options import test_options

import time

class BB_Editor(object):

    CANCEL = '//*[@id="bottom_submitButtonRow"]/input[1]'
    SUBMIT = '//*[@id="bottom_submitButtonRow"]/input[2]'

    def __init__(self, driver):
        self.driver = driver

    def select_form(self, element, wait=None):
        """Selects the options dropdown menu for blackboard
        form items.

        Parameters
        ----------
        element : str
            User inputed title of form name

        wait : int
            Time to pause for page load to complete. Default is None

        Returns
        -------
        """
        self.driver.find_element_by_xpath('//a[@title=' + "\"" + element + " item options" + "\"" ']').click()
        if wait is not None:
            time.sleep(wait)

    def check_state(self, xpath):
        """Checks the state of a given element, returns
        its boolean value.

        Parameters
        ----------
        xpath : str
            Raw xpath formatted as string value. Should be using
            global variable from assignment_options/test_options

        Returns
        -------
        boolean
            Returns 'True' if element is selected, and 'False' otherwise
        """
        x = self.driver.find_element_by_xpath(xpath)
        if x.is_selected() == True:
            return True
        return False

    def set_state(self, xpath, state):
        """Sets the desired state of an element.

        Parameters
        ----------
        xpath : str
            Raw xpath formatted as string value. Should be using
            global variable from assignment_options/test_options

        state : bool
            The user's desired state for the given element

        Returns
        -------
        """
        if self.check_state(xpath) != state:
            self.driver.find_element_by_xpath(xpath).click()

    def open_test_new_windows(self):
        return

    def make_link_available(self):
        return

    def create_announcement(self):
        return

    def start_restrict(self):
        return

    def end restrict(self):
        return

    def late_submission(self):
        return

    def due_date(self, state, date, time, wait):
        current_state = self.check_state(test_options.DUE_DATE_CHECK)
        if current_state == state:
            print('nothing to do here')
            return True
        if current_state:
            self.driver.find_element_by_xpath(test_options.DUE_DATE_VALUE).send_keys(date)
            self.driver.find_element_by_xpath(test_options.DUE_DATE_TIME).send_keys(time)

    def multiple_attempts(self):
        return

    def force_completion(self):
        return

    def cancel(self, wait=None):
        try:
            self.driver.find_element_by_xpath(BB_Editor.CANCEL).click()
            if wait is not None:
                time.sleep(wait)
        except:
            return False

    def submit(self, wait=None):
        try:
            self.driver.find_element_by_xpath(BB_Editor.SUBMIT).click()
            if wait is not None:
                time.sleep(wait)
        except:
            return False

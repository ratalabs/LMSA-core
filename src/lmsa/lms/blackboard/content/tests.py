"""
Handles any functionality related to editing 'Test' content items in
Blackboard
"""

from .options import test_options
from ..Library import Logic



class Tests(object):

    def __init__ (self, driver):
        self.driver = driver

    def open_test_in_new_window(self):
        return

    def make_link_available(self):
        return

    def create_announcement(self):
        return

    def multiple_attempts(self):
        return

    def force_completion(self):
        return

    def start_restrict(self, state, date, time):
        """Performs all operations related to the 'Start Restrict Date'. Order matters when invoking multiple
        'send_key' functions.

        Parameters
        ----------
        state : bool
            The desired state of the checkbox element (True/False)

        date : str
            The literal date value in the format mm/dd/yyyy

        time : str
            The literal time value in the format hh:mm AM/PM

        Returns
        -------
        """
        current_state = Logic(self.driver).check_state(test_options.START_RESTRICT_CHECK)
        if current_state != state:
            Logic(self.driver).set_state(xpath=test_options.START_RESTRICT_CHECK, dstate=state)
        if state:
            self.driver.find_element_by_xpath(test_options.START_RESTRICT_DATE).clear()
            self.driver.find_element_by_xpath(test_options.START_RESTRICT_TIME).clear()
            self.driver.find_element_by_xpath(test_options.START_RESTRICT_TIME).send_keys(time)
            self.driver.find_element_by_xpath(test_options.START_RESTRICT_DATE).send_keys(date)

    def end_restrict(self, state, date, time):
        """Performs all operations related to the 'End Restrict Date'. Order matters when invoking multiple
        'send_key' functions.

        Parameters
        ----------
        state : bool
            The desired state of the checkbox element (True/False)

        date : str
            The literal date value in the format mm/dd/yyyy

        time : str
            The literal time value in the format hh:mm AM/PM

        Returns
        -------
        """
        current_state = Logic(self.driver).check_state(test_options.END_RESTRICT_CHECK)
        if current_state != state:
            Logic(self.driver).set_state(xpath=test_options.END_RESTRICT_CHECK, dstate=state)
        if state:
            self.driver.find_element_by_xpath(test_options.END_RESTRICT_DATE).clear()
            self.driver.find_element_by_xpath(test_options.END_RESTRICT_TIME).clear()
            self.driver.find_element_by_xpath(test_options.END_RESTRICT_TIME).send_keys(time)
            self.driver.find_element_by_xpath(test_options.END_RESTRICT_DATE).send_keys(date)

    def due_date(self, state, date, time):
        """Performs all operations related to Due Dates. Order matters when invoking multiple
        'send_key' functions.

        Parameters
        ----------
        state : bool
            The desired state of the checkbox element (True/False)

        date : str
            The literal date value in the format mm/dd/yyyy

        time : str
            The literal time value in the format hh:mm AM/PM

        Returns
        -------
        """
        current_state = Logic(self.driver).check_state(test_options.DUE_DATE_CHECK)
        if current_state != state:
            Logic(self.driver).set_state(xpath=test_options.DUE_DATE_CHECK, dstate=state)
        if state:
            self.driver.find_element_by_xpath(test_options.DUE_DATE_VALUE).clear()
            self.driver.find_element_by_xpath(test_options.DUE_DATE_TIME).clear()
            self.driver.find_element_by_xpath(test_options.DUE_DATE_TIME).send_keys(time)
            self.driver.find_element_by_xpath(test_options.DUE_DATE_VALUE).send_keys(date)

    def late_submission(self):
        return

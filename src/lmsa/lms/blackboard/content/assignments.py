"""
Handles any functionality related to editing 'Assignment' content items in
Blackboard
"""

from .options import assignment_options
from ..Library import Logic


class Assignments(object):

    def __init__ (self, driver):
        self.driver = driver

    def due_date(self):
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
        current_state = self.check_state(assignment_options.DUE_DATE_CHECK)
        if current_state != state:
            self.set_state(xpath=assignment_options.DUE_DATE_CHECK, dstate=state)
        if state:
            self.driver.find_element_by_xpath(assignment_options.DUE_DATE_VALUE).clear()
            self.driver.find_element_by_xpath(assignment_options.DUE_DATE_TIME).clear()
            self.driver.find_element_by_xpath(assignment_options.DUE_DATE_TIME).send_keys(time)
            self.driver.find_element_by_xpath(assignment_options.DUE_DATE_VALUE).send_keys(date)


    def points_possible(self):
        return

    def start_limit_availability(self, state, date, time):
        """Performs all operations related to the 'Start Limit Availability'. Order matters when invoking multiple
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
        current_state = Logic(self.driver).check_state(assignment_options.START_LIMIT_AVAILABILITY_CHECK)
        if current_state != state:
            Logic(self.driver).set_state(xpath=assignment_options.START_LIMIT_AVAILABILITY_CHECK, dstate=state)
        if state:
            self.driver.find_element_by_xpath(assignment_options.START_LIMIT_AVAILABILITY_DATE).clear()
            self.driver.find_element_by_xpath(assignment_options.START_LIMIT_AVAILABILITY_TIME).clear()
            self.driver.find_element_by_xpath(assignment_options.START_LIMIT_AVAILABILITY_TIME).send_keys(time)
            self.driver.find_element_by_xpath(assignment_options.START_LIMIT_AVAILABILITY_DATE).send_keys(date)

    def end_limit_availability(self, state, date, time):
        """Performs all operations related to the 'End Limit Availability'. Order matters when invoking multiple
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
        current_state = Logic(self.driver).check_state(assignment_options.END_LIMIT_AVAILABILITY_CHECK)
        if current_state != state:
            Logic(self.driver).set_state(xpath=assignment_options.END_LIMIT_AVAILABILITY_CHECK, dstate=state)
        if state:
            self.driver.find_element_by_xpath(assignment_options.END_LIMIT_AVAILABILITY_DATE).clear()
            self.driver.find_element_by_xpath(assignment_options.END_LIMIT_AVAILABILITY_TIME).clear()
            self.driver.find_element_by_xpath(assignment_options.END_LIMIT_AVAILABILITY_TIME).send_keys(time)
            self.driver.find_element_by_xpath(assignment_options.END_LIMIT_AVAILABILITY_DATE).send_keys(date)

    def track_number_of_views(self):
        return

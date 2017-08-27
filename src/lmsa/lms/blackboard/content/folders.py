"""
Handles any functionality related to editing 'Folder' content items in
Blackboard
"""

from .options import folder_options
from ..Library import Logic

class Folders(object):

    def __init__ (self, driver):
        self.driver = driver

    def content_view(self):
        return

    def permit_users_to_view(self):
        return

    def track_number_of_views(self):
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
        current_state = Logic(self.driver).check_state(folder_options.START_RESTRICT_CHECK)
        if current_state != state:
            Logic(self.driver).set_state(xpath=folder_options.START_RESTRICT_CHECK, dstate=state)
        if state:
            self.driver.find_element_by_xpath(folder_options.START_RESTRICT_DATE).clear()
            self.driver.find_element_by_xpath(folder_options.START_RESTRICT_TIME).clear()
            self.driver.find_element_by_xpath(folder_options.START_RESTRICT_TIME).send_keys(time)
            self.driver.find_element_by_xpath(folder_options.START_RESTRICT_DATE).send_keys(date)
        return

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
        current_state = Logic(self.driver).check_state(folder_options.END_RESTRICT_CHECK)
        if current_state != state:
            Logic(self.driver).set_state(xpath=folder_options.END_RESTRICT_CHECK, dstate=state)
        if state:
            self.driver.find_element_by_xpath(folder_options.END_RESTRICT_DATE).clear()
            self.driver.find_element_by_xpath(folder_options.END_RESTRICT_TIME).clear()
            self.driver.find_element_by_xpath(folder_options.END_RESTRICT_TIME).send_keys(time)
            self.driver.find_element_by_xpath(folder_options.END_RESTRICT_DATE).send_keys(date)

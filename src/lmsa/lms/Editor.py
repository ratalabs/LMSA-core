"""
Top level editing methods.

Will check 'type' of html element and based on 'type' perform,
proper operations.

Will perform logic handling, and potentionally even perform multiple checks
to assure that check states are 'actually changed'. This has been an issue in the past,
where if I toggled a checkbox state to TRUE and a couple lines later I checked the box
I just changed it's return state would be FALSE, even though it's visibly checked.

"""

from lmsa.lms.blackboard.options import *

class LMS_Editor(object):

    def __init__(self, driver):
        self.driver = driver

    def check_type(self, val):
        """
        Returns the type of an element provided to it.
        """
        return self.driver.find_element_by_xpath(val).get_attribute('type')

    def check_state(self, xpath):
        """
        Returns that state (True/False) of the provided element
        """
        x = self.driver.find_element_by_xpath(xpath)
        if x.is_selected() == True:
            return True
        return False

    def edit(self, element = None, state = None, val = None, **kwargs):
        """
        Dynamically handles edit requests.
        """
        type = self.check_type(element)
        #basic structure, I think
        if type == 'text':
            self.edit_text(element, val)
        elif type == 'radio':
            self.edit_radio()
        elif type == 'checkbox':
            self.edit_checkbox()

    def edit_text(self, element, val):
        self.driver.find_element_by_xpath(element).send_keys(val)
        return

    def edit_radio(self):
        return

    def edit_checkbox(self, element, state):
        if state != self.check_state(element):
            self.driver.find_element_by_xpath(element).click()
        return

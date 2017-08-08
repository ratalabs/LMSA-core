"""
Handles any editing operations unique to the Blackboard LMS
"""

from lmsa.lms.blackboard.options import assignment_options
from lmsa.lms.blackboard.options import test_options

import time

class BB_Editor(object):

    def __init__(self, driver):
        self.driver = driver

    def select_form(self, element, wait=None):
        self.driver.find_element_by_xpath('//a[@title=' + "\"" + element + " item options" + "\"" ']').click()
        if wait is not None:
            time.sleep(wait)

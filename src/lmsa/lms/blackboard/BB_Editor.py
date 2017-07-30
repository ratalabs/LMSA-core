"""
Derived from LMS Editor

Handles any editing operations unique to the Blackboard LMS
"""

from lsma.lms.Editor import LMS_Editor

class BB_Editor(LMS_Editor):

    def __init__(self, driver):
        self.driver = driver

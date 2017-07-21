#!/usr/bin/env python
#-*- coding: utf-8 -*-

import selenium
import time
from selenium import webdriver as wbd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Editor(object):

    def __init__(self, driver):
        self.driver = driver

    def assignmentSelector(self, element, wait = None):
        """
        Selects (clicks) the desired assignment/test.

        :Args:
        -   element: The element, or name, of the content item you wish to clicks.
        -   wait: Specifies time to wait after action.
            If None, does nothing.
        """
        try:
            self.driver.find_element_by_xpath('//a[@title=' + "\"" + element + " item options" + "\"" ']').click()
            time.sleep(wait)
        except:
            print("Error with " + element + "...skipping")
            return False
        else:
            return True

    def editTestOptions(self, wait = None):
        """
        Clicks the 'Edit Test Options Button' for entering the edit options menu.

        :Args:
        -   wait: Specifies time to wait after action.
            If None, does nothing.
        """
        try:
            self.driver.find_element_by_xpath('//a[@title="Edit the Test Options"]').click()
            time.sleep(wait)
        except Exception as e:
            pass
        else:
            return True

    def startRestrictCheck(self, state, wait = None):
        try:
            if state:
               self.driver.find_element_by_id('start_restrict').click()
               time.sleep(wait)
            else:
               pass
        except Exception as e:
            pass

    def endRestrictCheck(self, state, wait = None):
        try:
            if state:
                self.driver.find_element_by_id('end_restrict').clear()
                self.driver.find_element_by_id('end_restrict').click()
                time.sleep(wait)
            else:
                self.driver.find_element_by_id('end_restrict').clear()
                time.sleep(wait)
        except Exception as e:
            pass

    def dueDateCheck(self, state, wait = None):
        try:
            if state:
                self.driver.find_element_by_id('_dueDate').click()
                time.sleep(wait)
        except Exception as e:
            pass

    def lateSubmissionCheck(self, state, wait = None):
        try:
            if state:
                self.driver.find_element_by_id('doNotAllowLateSubmission').click()
                time.sleep(wait)
            else:
                pass
        except Exception as e:
            pass

    def dueDate(self, date, wait = None):
        try:
            self.driver.find_element_by_id('dp_dueDate_date').clear()
            self.driver.find_element_by_id('dp_dueDate_date').send_keys(date)
            time.sleep(wait)
        except Exception as e:
            pass

    def dueDateTime(self, time, wait = None):
        try:
            driver.find_element_by_id('tp_dueDate_time').clear()
            driver.find_element_by_id('tp_dueDate_time').send_keys(time)
            time.sleep(wait)
        except Exception as e:
            pass

    def cancel(self, wait = None):
        try:
            self.driver.find_element_by_name('bottom_Cancel').click()
            time.sleep(wait)
        except Exception as e:
            pass

    def submit(self, wait = None):
        try:
            self.driver.find_element_by_name('bottom_submit').click()
            time.sleep(wait)
        except Exception as e:
            pass


class TestOptions(Editor):

    def __init__(self):
        return

class AssignmentOptions(Editor):

    def __init__(self):
        return

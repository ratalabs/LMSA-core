#!/usr/bin/env python
# -*- coding: utf-8 -*-

import selenium
import time
from selenium import webdriver as wbd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EditTests(object):

    def __init__(self, driver):
        self.driver = driver

    def is_checked(self, item):
        return self.driver.execute_script(("return document.getElementById('%s').checked") % item)

    def assignmentSelector(self, element, wait = None, **kwargs):
        try:
            self.driver.find_element_by_xpath('//a[@title=' + "\"" + element + " item options" + "\"" ']').click()
            time.sleep(wait)
        except:
            print("Error with " + element + "...skipping")
        finally:
            pass

    def editTestOptions(self, wait = None):
        try:
            self.driver.find_element_by_xpath('//a[@title="Edit the Test Options"]').click()
            time.sleep(wait)
        except Exception as e:
            pass

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
        #element = self.is_checked('_dueDate')
        #while element:
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

    def is_checked(self, item):
        checked = self.driver.execute_script(("return document.getElementById('%s').checked") % item)
        return checked

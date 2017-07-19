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

    def assignmentSelector(self, element, wait = None):
        try:
            self.driver.find_element_by_xpath('//a[@title=' + "\"" + element + " item options" + "\"" ']').click()
            #driver.find_element_by_xpath('//a[@title=' + "\"" + test + " item options" + "\"" ']').click()
        except :
            print("Error with " + module + " : " + test + "...skipping")
            return False
        finally:
            pass

    def edit_test_options(self, wait = None):
        try:
            self.driver.find_element_by_xpath('//a[@title="Edit the Test Options"]').click()
            time.sleep(wait)
        except Exception as e:
            pass

    def start_restrict(driver, state, **kwargs):
        try:
            if state:
               driver.find_element_by_id('start_restrict').click()
            else:
               pass
        except Exception as e:
            pass


    def end_restrict(driver, state, **kwargs):
        try:
            if state:
                driver.find_element_by_id('end_restrict').clear()
                driver.find_element_by_id('end_restrict').click()
            else:
                driver.find_element_by_id('end_restrict').clear()
        except Exception as e:
            pass

    def _dueDate(driver, state, **kwargs):
        try:
            if state:
                #element = driver.find_element_by_name('due_date_in_use')
                driver.find_element_by_id('_dueDate').click()
        except Exception as e:
            pass

    def _lateSubmission(driver, state, **kwargs):
        try:
            if state:
                driver.find_element_by_id('doNotAllowLateSubmission').click()
                #while str(driver.execute_script("return document.getElementById('doNotAllowLateSubmission').checked")) == 'False':
                #    element = driver.find_element_by_name('doNotAllowLateSubmission')
                #    element.click()
            else:
                pass
        except Exception as e:
            pass

    def dp_dueDate_date(driver, date, **kwargs):
        try:
            driver.find_element_by_id('dp_dueDate_date').clear()
            driver.find_element_by_id('dp_dueDate_date').send_keys(date)
        except Exception as e:
            pass

    def tp_dueDate_time(driver, time, **kwargs):
        try:
            driver.find_element_by_id('tp_dueDate_time').clear()
            driver.find_element_by_id('tp_dueDate_time').send_keys(time)
        except Exception as e:
            pass

    def cancel(driver, **kwargs):
        try:
            driver.find_element_by_name('bottom_Cancel').click()
        except Exception as e:
            pass

    def submit(driver, **kwargs):
        try:
            driver.find_element_by_name('bottom_submit').click()
        except Exception as e:
            pass

    def main():
        try:
            errorHandler1()
            return 0
        except Exception as e:
            raise

    def errorHandler1():
        raise RuntimeError('this is the error message')

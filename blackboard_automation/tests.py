### Python 2.7 required
### Author: Sam McCaffrey
### Purpose: Automate BB Tasks

import selenium
import getpass
import time
import pandas as pd
from selenium import webdriver as wbd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def assignmentPicker(driver, test, module, **kwargs):
    try:
        driver.find_element_by_xpath('//a[@title=' + "\"" + test + " item options" + "\"" ']').click()
    except Exception as e:
        print("Error with " + module + " : " + test + "...skipping")
        pass

def edit_test_options(driver):
    try:
        driver.find_element_by_xpath('//a[@title="Edit the Test Options"]').click()
    except Exception as e:
        pass

def start_restrict(driver, state):
    try:
        bl = is_checked(driver, start_restrict)
        print (bl)
        print("other: " + bl)
        driver.find_element_by_id('start_restrict').click()

        #if not state: # remove 'not' before final compile
        #    driver.find_element_by_id('start_restrict').click()
        #else:
        #    pass
    except Exception as e:
        pass

def is_checked(self, driver, item):
  checked = driver.execute_script(("return document.getElementById('%s').checked") % item)
  return checked

def end_restrict(driver, state):
    try:
        if state:
            driver.find_element_by_id('end_restrict').clear()
            driver.find_element_by_id('end_restrict').click()
        else:
            driver.find_element_by_id('end_restrict').clear()
    except Exception as e:
        pass

def _dueDate(driver, state):
    try:
        bl = driver.find_element_by_id('_dueDate').is_selected()
        print(str(bl))
        if bl:
            driver.find_element_by_id('_dueDate').double_click()
        #if state is True and str(bl) == 'False':
        #    driver.find_element_by_id('_dueDate').click()
        #elif state is not True and str(bl) == 'True':
        #    driver.find_element_by_id('_dueDate').click()
        #elif state is not True and str(bl) == 'False':
        #    pass
    except Exception as e:
        pass

def _lateSubmission(driver, state):
    try:
        if not state:
            driver.find_element_by_id('doNotAllowLateSubmission').click()
        else:
            pass
    except Exception as e:
        pass

def dp_dueDate_date(driver, date):
    try:
        driver.find_element_by_id('dp_dueDate_date').clear()
        driver.find_element_by_id('dp_dueDate_date').send_keys(date)
    except Exception as e:
        pass

def cancel(driver):
    try:
        driver.find_element_by_name('bottom_Cancel').click()
    except Exception as e:
        pass

def errorHandler1():
    return

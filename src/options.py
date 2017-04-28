### Python 2.7 required
### Author: Sam McCaffrey
### Purpose: Automate BB Tasks

import selenium
import getpass
import time
import xlrd
import pandas as pd
from collections import OrderedDict
from selenium import webdriver as wbd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def assignmentPicker(d, prelab, n):
    try:
        d.find_element_by_xpath('//a[@title=' + "\"" + prelab + " item options" + "\"" ']').click()
    except Exception as e:
        print("Error with " + prelab + "...skipping")
        pass

def edit_test_options(d):
    try:
        d.find_element_by_xpath('//a[@title="Edit the Test Options"]').click()
    except Exception as e:
        pass

def start_restrict(d,state):
    try:
        if state:
            d.find_element_by_id('start_restrict').click()
        else:
            pass
    except Exception as e:
        pass

def end_restrict(d,state):
    try:
        if state:
            d.find_element_by_id('end_restrict').click()
        else:
            pass
    except Exception as e:
        pass

def _dueDate(d,state):
    try:
        if not state:
            d.find_element_by_id('_dueDate').click()
        else:
            pass
    except Exception as e:
        pass

def _lateSubmission(d,state):
    try:
        if not state:
            d.find_element_by_id('doNotAllowLateSubmission').click()
        else:
            pass
    except Exception as e:
        pass

def dp_dueDate_date(d, date):
    try:
        d.find_element_by_id('dp_dueDate_date').clear()
        d.find_element_by_id('dp_dueDate_date').send_keys(date)
    except Exception as e:
        pass

def cancel(d):
    try:
        d.find_element_by_name('bottom_Cancel').click()
    except Exception as e:
        pass

def errorHandler1():
    return

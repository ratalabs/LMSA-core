#!/usr/bin/env python
#-*- coding: utf-8 -*-

import selenium
import time
from selenium import webdriver as wbd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def assignmentSelector(driver, assignment, module, **kwargs):
    try:
        driver.find_element_by_xpath('//a[@title=' + "\"" + assignment + " item options" + "\"" ']').click()
    except Exception as e:
        print("Error with " + module + " : " + assignment + "...skipping")
        pass

def edit_test_options(driver, **kwargs):
    try:
        driver.find_element_by_xpath('//a[@title="Edit"]').click()
    except Exception as e:
        pass

def start_restrict(driver,state):
    try:
        if state:
            driver.find_element_by_id('start_restrict').click()
        else:
            pass
    except Exception as e:
        pass

def end_restrict(driver,state):
    try:
        if state:
            driver.find_element_by_id('end_restrict').click()
        else:
            pass
    except Exception as e:
        pass

def _dueDate(driver,state):
    try:
        if not state:
            driver.find_element_by_id('_dueDate').click()
        else:
            pass
    except Exception as e:
        pass

def _lateSubmission(driver,state):
    try:
        if not state:
            driver.find_element_by_id('doNotAllowLateSubmission').click()
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

def submit(driver, **kwargs):
    try:
        driver.find_element_by_name('bottom_submit').click()
    except Exception as e:
        pass

def cancel(driver, **kwargs):
    try:
        driver.find_element_by_name('bottom_Cancel').click()
    except Exception as e:
        pass

def errorHandler1():
    return

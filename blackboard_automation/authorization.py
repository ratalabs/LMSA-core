#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getpass
import time

#lass login():
#    def __init__(self):
#        self.driver = driver
#        self.url = url
#        self.time = time

def login(driver, url, wait = None, **kwargs):
    uname = raw_input("Enter ASURITE username: ")
    pword = getpass.getpass("Enter ASURITE password: ")
    try:
        driver.get(url)
        driver.find_element_by_id('username').send_keys(uname)
        driver.find_element_by_id('password').send_keys(pword)
        driver.find_element_by_class_name('submit').click()
        time.sleep(wait)
    except Exception as e:
        print e
        pass

def dual_factor(driver, wait = None, **kwargs):
    try:
        driver.find_element_by_class_name('positive auth-button').click()
        time.sleep(wait)
    except:
        pass

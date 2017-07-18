#!/usr/bin/env python
# -*- coding: utf-8 -*-

import selenium
import time
from selenium import webdriver as wbd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""
    Create an object to check the state of any boolean element
"""
class IsChecked(self, driver, element):

    def __init__(self):
        self.element = element
        self.driver = driver

    def is_checked(self, driver, item, **kwargs):
        checked = driver.execute_script(("return document.getElementById('%s').checked") % item)
        return checked

#!/usr/bin/env python
#-*- coding: utf-8 -*-

import selenium
import time
from selenium import webdriver as wbd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SideBar(object):

    def __init__(self, driver, wait = None):
        self.driver = driver
        self.wait = wait

    def navigate(self, element):
        try:
            self.driver.find_element_by_link_text(element).click()
            #driver.find_element_by_link_text(module).click()
        except Exception as e:
            pass

#!/usr/bin/env python
#-*- coding: utf-8 -*-

import selenium
import time
from selenium import webdriver as wbd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def navigate(driver, module, wait = None, **kwargs):
    try:
        driver.find_element_by_link_text(module).click()
    except Exception as e:
        pass

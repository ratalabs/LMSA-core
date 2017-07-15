#!/usr/bin/env python
#-*- coding: utf-8 -*-

import selenium
import time
from selenium import webdriver as wbd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@classmethod
def find(cls, query, selector = 'id', catch_all = False):
    if catch_all:
        finder = 'find_elements_by_'
    else:
        finder = 'find_element_by_'

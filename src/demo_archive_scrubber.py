### Python 2.7 required
### Author: Sam McCaffrey
### Purpose: Crawl Old archive

import selenium
import getpass
import time
import xlrd
import numpy as np
import simplejson as json
from collections import OrderedDict
from selenium import webdriver as wbd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

### Creates the browser instance in which all operations take place ###
driver = wbd.Chrome('~/Desktop/git/lib/chromedriver')

driver.get("http://pirt-archive.asu.edu/")

### Next scrub all data

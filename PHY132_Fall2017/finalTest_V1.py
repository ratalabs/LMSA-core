import selenium
import getpass
import time
import logging as log
import pandas as pd
from selenium import webdriver as wbd
from selenium.webdriver.common.by import By

import sys
sys.path.append('/Users/smccaffrey/Desktop/git/blackboard_automation')

from blackboard_automation import tests
from blackboard_automation import assignments as lab_reports

### Creates the browser instance in which all operations take place ###
driver = wbd.Chrome('/Users/smccaffrey/Desktop/git/blackboard_automation/lib/chromedriver2.26')

### Specify global Variables ###
filename = '/Users/smccaffrey/Desktop/git/blackboard_automation/PHY132_Fall2017/FinalLabTest.info.csv'
p = 'PHY 132: University Physics Lab II (2017 Fall)-'
URL = 'https://myasucourses.asu.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1'

### Parsers excel workbook (must be .csv file) ###
def parser(filename):
    df1 = pd.read_csv(filename, dtype=object, delimiter=',', header=None)
    return df1

### Authenticates MyASU credentials ###
def authorization(d, URL, username=None, t=15):
    if not username:
        username = raw_input("Enter ASURITE username: ")
    password = getpass.getpass("Enter ASURITE password: ")

    #URL = 'https://myasucourses.asu.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1'

    d.get(URL)
    d.find_element_by_id("username").send_keys(username)
    d.find_element_by_id("password").send_keys(password)
    d.find_element_by_class_name('submit').click()

    time.sleep(t) #Gives you time for 2-Step Authentication

### Update FinalLabTest information ###
def updater(d, p, URL, arr, module, dryrun=True):
    i = 1
    for i in range(1, len(arr[0])):
        time.sleep(5)
        d.find_element_by_link_text(p + str(arr[0][i])).click()
        time.sleep(5)
        d.find_element_by_link_text(module).click()
        time.sleep(5)
        d.find_element_by_link_text('Course Tools').click()
        time.sleep(2)
        d.find_element_by_link_text('Respondus LockDown Browser').click()
        time.sleep(2)
        d.find_element_by_xpath('//img[@alt="Menu for exam Final Lab Test- Requires Respondus LockDown Browser"]').click()
        time.sleep(2)
        d.find_element_by_link_text('Modify Settings').click()
        time.sleep(2)
        d.find_element_by_id('ldbEnabled').click()
        d.find_element_by_id('testPassword').clear()
        d.find_element_by_id('testPassword').send_keys(str(arr[3][i]))

        if not dryrun:
            d.find_element_by_class_name('applySettings').click()
        d.find_element_by_class_name('closeSettings').click()

        d.get(URL)

### test function ###
def test_func(d, filename, dryrun=False):
    parser(filename)
    if not dryrun:
        authorization(d, URL)
        updater(d, p, URL, parser(filename), module = 'FINAL Lab Test')
test_func(driver, filename)

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


### Creates the browser instance in which all operations take place ###
driver = wbd.Chrome('/Users/smccaffrey/Desktop/git/PIRT_ASU/lib/chromedriver')
filename = '/Users/smccaffrey/Desktop/git/PIRT_ASU/testing/Workbook1.csv'

p = 'PHY 114: General Physics Laboratory (2016 Fall)-'

### Parsers excel workbook (must be .csv file) ###
def parser(filename):
    df1 = pd.read_csv(filename, dtype=object, delimiter=',', header=None)
    #print(len(df1.columns)-3)
    #print(len(df1['Section']))
    print(df1[3][3])
    return df1

### Authenticates MyASU credentials ###
def authorization(d, username=None, t=15):
    """Handles dual factor authentication.

    Parameters
    ----------
    d : str
        Path to driver binary (defaults to packaged chrome)
    username : str
        Username to log in with
    time : int
        number of seconds to wait for authentication (default 15)
    """
    if not username:
        username = raw_input("Enter ASURITE username: ")
    password = getpass.getpass("Enter ASURITE password: ")

    URL = 'https://myasucourses.asu.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1'

    d.get(URL)
    d.find_element_by_id("username").send_keys(username)
    d.find_element_by_id("password").send_keys(password)
    d.find_element_by_class_name('submit').click()

    time.sleep(t) #Gives you time for 2-Step Authentication

### various functions within page
def start_restrict(d,state):
    if state:
        d.find_element_by_id('start_restrict').click()
    else:
        pass
def end_restrict(d,state):
    if state:
        d.find_element_by_id('end_restrict').click()
    else:
        pass
def _dueDate(d,state):
    if not state:
        d.find_element_by_id('_dueDate').click()
    else:
        pass
def _lateSubmission(d,state):
    if not state:
        d.find_element_by_id('doNotAllowLateSubmission').click()
    else:
        pass



### Update Prelabs information ###
def updater(d, p, arr, dryrun=True):
    i = 0
    for i in range(1, len(arr['Section'])):
        d.find_element_by_link_text(p+str(arr['Section'][i])).click()
        time.sleep(5)
        d.find_element_by_link_text('PRELABS').click()
        time.sleep(5)
        for i in range (1, len(arr.columns)-13):
            d.find_element_by_xpath('//a[@title=' + str(arr[i+3][0]) + '" item options"]').click()
            time.sleep(5)
            d.find_element_by_xpath('//a[@title="Edit the Test Options"]').click()

            d.find_element_by_id('start_restrict')





### test function ###
def test_func(d, filename, dryrun=True):
    parser(filename)
    d.quit()
    if not dryrun:
        authorization(d)
        updater(d, p, parser(filename))
        d.quit()

test_func(driver, filename)

#need to click href within item
#int(string.split('-')[-1]) building section list

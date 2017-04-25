### Python 2.7 required
### Author: Sam McCaffrey
### Purpose: Automate BB Tasks

import selenium
import getpass
import time
import xlrd
from collections import OrderedDict
from selenium import webdriver as wbd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

### Creates the browser instance in which all operations take place ###
driver = wbd.Chrome('/Users/smccaffrey/Desktop/git/PIRT_ASU/lib/chromedriver')
filename = '/Users/smccaffrey/Desktop/git/PIRT_ASU/testing/Workbook1.csv'

p = 'PHY 114: General Physics Laboratory (2016 Fall)-'

### Parsers excel workbook ###
def parse(filename):
    """Parses an XLSX workbook into an Ordered Dictionary
    Parameters
    ----------
    filename : str
        Path to filename
    Returns
    -------
    list
        Inventory list
    """
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_index(0)

    due_dates = []

    for rownum in range(1,sh.nrows):
        dates = OrderedDict()
        row_values = sh.row_values(rownum)
        dates['Section'] = row_values[0]
        dates['Prelab_Due_Time'] = row_values[1]
        dates['Lab_Report_Due_Time'] = row_values[2]
        dates['1D_Motion_Prelab'] = row_values[3]
        dates['1D_UALM_Prelab'] = row_values[4]
        dates['Vectors_and_Statics_Prelab'] = row_values[5]
        dates['N2L_Prelab'] = row_values[6]
        dates['Circular_Motion_Prelab'] = row_values[7]
        dates['Friction_Prelab'] = row_values[8]
        dates['C_of_E_Prelab'] = row_values[9]
        dates['Static_Torque_Prelab'] = row_values[10]
        dates['Rotational_Motion_Prelab'] = row_values[11]
        dates['1D_Motion_Lab_Report'] = row_values[12]
        dates['1D_UALM_Lab_Report'] = row_values[13]
        dates['Vectors_and_Statics_Lab_Report'] = row_values[14]
        dates['N2L_Lab_Report'] = row_values[15]
        dates['Circular_Motion_Lab_Report'] = row_values[16]
        dates['Friction_Lab_Report'] = row_values[17]
        dates['C_of_E_Lab_Report'] = row_values[18]
        dates['Static_Torque_Lab_Report'] = row_values[19]
        dates['Rotational_Motion_Lab_Report'] = row_values[20]

        due_dates.append(dates)

    return due_dates

def parser(filename):
    df1 = pd.read_csv(filename, dtype=object, header=0)
    print df1.shape
    print['Prelab_Due_Time'][0]
    print df1
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

### Update Prelabs information ###
def updater(d, p, arr, dryrun=True):
    i = 0
    for i in range(1, len(arr['Section'])):
        d.find_element_by_link_text(p+str(arr['Section'][i])).click()
        time.sleep(5)
        d.find_element_by_link_text('PRELABS').click()
        time.sleep(5)

        d.find_element_by_xpath('//a[@title="Prelab: Absorption of Nuclear Radiation item options"]').click()
        time.sleep(5)
        d.find_element_by_xpath('//a[@title="Edit the Test Options"]').click()


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

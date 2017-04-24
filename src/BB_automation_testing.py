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

### Creates the browser instance in which all operations take place ###
driver = wbd.Chrome('~/Desktop/git/lib/chromedriver')

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

### Authenticates MyASU credentials ###
def authorization(d, username=None, time=15):
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

    URL = 'https://weblogin.asu.edu/cas/login?service=https%3A%2F%2Fdev-pirt-16.ws.asu.edu%2Fcas%3Fdestination%3Dnode%2F3'

    d.get(URL)
    d.find_element_by_id("username").send_keys(username)
    d.find_element_by_id("password").send_keys(password)
    d.find_element_by_class_name('submit').click()

    time.sleep(time) #Gives you time for 2-Step Authentication

### Update Prelabs information ###


#need to click href within item
#int(string.split('-')[-1]) building section list

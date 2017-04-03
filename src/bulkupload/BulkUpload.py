### Python 2.7 required
### Author: Sam McCaffrey
### Purpose: Bulk upload of new inventory items

import selenium
import getpass
import time
import xlrd
from collections import OrderedDict
from selenium import webdriver as wbd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#driver = wbd.Chrome('lib/chromedriver')

def get_driver(path, driver_type='chrome'):
    """Returns driver object

    Parameters
    ----------
    path : str
        Path to driver
    Returns
    -------
    Driver
    """
    drivers = {'chrome': wbd.Chrome,
               'firefox': wbd.FireFox}

    return drivers[driver_type.lower()](path)

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

    inventory_list = []

    for rownum in range(1, sh.nrows):
	   inventory = OrderedDict()
	   row_values = sh.row_values(rownum)
	   inventory['Item'] = row_values[0]
	   inventory['Location'] = row_values[1]
	   inventory['Quantity'] = row_values[2]
	   inventory['Description'] = row_values[3]
	   inventory_list.append(inventory)

    return inventory_list

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

    time.sleep(time)


def upload(inventory_list, d, indices=None, dryrun=True):
    """Adds data from array to all respective fields

    Parameters
    ----------
    invetory_list : [OrderedDict]
        Array-like of OrderedDicts containing item information

    d : Driver
        Selenium driver object

    Keyword Args
    ------------
    indices : [int]
        List of indices to iterate through

    dryrun : bool
        ``True`` to not submit the changes
    """

    top_URL = "https://dev-pirt-16.ws.asu.edu/node/add/inventory-item"

    for i in indices:
        d.get(top_URL)
        d.find_element_by_id("edit-title").send_keys(inventory_list[i]['Item'])
        d.find_element_by_id("edit-field-activity-type-und-lab").click()
        d.find_element_by_class_name("fieldset-title").click()
        d.find_element_by_id("edit-field-room-number-und-0-value").send_keys(inventory_list[i]['Location'])
        d.find_element_by_id("edit-field-item-count-und-0-value").send_keys(int(inventory_list[i]['Quantity'])) #Joe made this line work
        d.find_element_by_id("wysiwyg-toggle-edit-body-und-0-value").click()
        d.find_element_by_id("edit-body-und-0-value").send_keys(inventory_list[i]['Description'])
        if not dryrun:
            d.find_element_by_id("edit-submit").click()
        time.sleep(4)

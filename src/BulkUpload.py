### Python 2.7 required
### Author: Sam McCaffrey
### Purpose: Bulk upload of new inventory items

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

driver = wbd.Chrome('lib/chromedriver')

### Parses an XLSX workbook into an Ordered Dictionary
def parser():
    wb = xlrd.open_workbook('testing/test.xlsx')
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

def authorization(d):
    username = raw_input("Enter ASURITE username: ")
    password = getpass.getpass("Enter ASURITE password: ")

    d.get('https://weblogin.asu.edu/cas/login?service=https%3A%2F%2Fdev-pirt-16.ws.asu.edu%2Fcas%3Fdestination%3Dnode%2F3')

    d.find_element_by_id("username").send_keys(username)
    d.find_element_by_id("password").send_keys(password)
    d.find_element_by_class_name('submit').click()

    time.sleep(15) #Gives you time for 2-Step Authentication

    return

def upload(d,y,i):
    d.get("https://dev-pirt-16.ws.asu.edu/node/add/inventory-item")
    d.find_element_by_id("edit-title").send_keys(y[i]['Item'])
    d.find_element_by_id("edit-field-activity-type-und-lab").click()
    d.find_element_by_class_name("fieldset-title").click()
    d.find_element_by_id("edit-field-room-number-und-0-value").send_keys(y[i]['Location'])
    d.find_element_by_id("edit-field-item-count-und-0-value").send_keys(int(y[i]['Quantity'])) #Joe made this line work
    d.find_element_by_id("wysiwyg-toggle-edit-body-und-0-value").click()
    d.find_element_by_id("edit-body-und-0-value").send_keys(y[i]['Description'])
    #Only Uncomment this when you're actually ready to submit
    #d.find_element_by_id("edit-submit").click()
    time.sleep(4)


### Run Program ###
authorization(driver)
i = 0
while i <= len(parser()):
    upload(driver,parser(),i)
    i += 1

'''Python 2.7 required'''

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

driver = wbd.Chrome('/Users/smccaffrey/Desktop/PIRT_uploader/chromedriver')

### Parses an XLSX workbook into an Ordered Dictionary
def parser():
    wb = xlrd.open_workbook('/Users/smccaffrey/Desktop/PIRT_uploader/test.xlsx')
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

def authorization():
    username = raw_input("Enter ASURITE username: ")
    password = getpass.getpass("Enter ASURITE password: ")

    driver.get('https://weblogin.asu.edu/cas/login?service=https%3A%2F%2Fdev-pirt-16.ws.asu.edu%2Fcas%3Fdestination%3Dnode%2F3')

    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_class_name('submit').click()
    
    time.sleep(15) #Gives you time for 2-Step Authentication
    
    return driver
    
def upload(x,y,i):
    x.get("https://dev-pirt-16.ws.asu.edu/node/add/inventory-item")
    x.find_element_by_id("edit-title").send_keys(y[i]['Item'])
    x.find_element_by_id("edit-field-activity-type-und-lab").click()
    x.find_element_by_class_name("fieldset-title").click()
    x.find_element_by_id("edit-field-room-number-und-0-value").send_keys(y[i]['Location'])
    x.find_element_by_id("edit-field-item-count-und-0-value").send_keys(int(y[i]['Quantity'])) #Joe made this line work
    x.find_element_by_id("wysiwyg-toggle-edit-body-und-0-value").click()
    x.find_element_by_id("edit-body-und-0-value").send_keys(y[i]['Description'])
    #Only Uncomment this when your actually ready to submit
    #x.find_element_by_id("edit-submit").click()
    time.sleep(4)


### Run Program ###
authorization()
i = 0
while i <= len(parser()):
    upload(driver,parser(),i)
    i += 1
    
    
        



		
	

	

	



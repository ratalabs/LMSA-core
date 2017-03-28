### Python 2.7 required
### Author: Sam McCaffrey
### Purpose: Automate BB Tasks

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

### Parsers excel workbook ###
def parser():
    wb = xlrd.open_workbook('testing/Workbook1.xlsx')
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
def authorization():
    username = raw_input("Enter ASURITE username: ")
    password = getpass.getpass("Enter ASURITE password: ")

    driver.get('https://weblogin.asu.edu/cas/login?service=https%3A%2F%2Fdev-pirt-16.ws.asu.edu%2Fcas%3Fdestination%3Dnode%2F3')

    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_class_name('submit').click()

    time.sleep(15) #Gives you time for 2-Step Authentication

    return

### Update Prelabs information ###
def prelab_update(d,y,i):
    return

### Update Lab Report information ###
def lab_update(d,y,i):
    return

### Cycle through all sections ###
def section_cycler(d,y,i):
    section = due_dates[i]['Section']
    d.find_elements_by_xpath('//*[contains(text(), "' + section + '")]')
    #need to click href within item
    pass

i = 0
while i <= len(parser()):

    #click each section
    #iterate through prelabs
    #Edit each prelab
    #then iterate through each lab
    #Edit each lab

"""Import python functionality"""
import sys
import time
import pandas as pd
from selenium import webdriver

"""Append Local file locations to to PYTHONPATH"""
sys.path.append('/Users/smccaffrey/Desktop/LMSA-core/src/')

"""Import LMSA functionality"""
from lmsa.manipulation.ASU.ASU_manipulator import ASU_manipulator
from lmsa.lms.blackboard.BlackBoard import Editor
from lmsa.lms.blackboard.content.tests import Tests
from lmsa.lms.blackboard.content.assignments import Assignments
from lmsa.lms.blackboard.content.folders import Folders
from lmsa.lms.blackboard.Library import Logic
from lmsa.lms.blackboard.Library import Window

"""Global Variables"""
filename = '/Users/smccaffrey/Desktop/LMSA-core/scripts/input/due_dates_template.csv'
prefix1 = 'PHY 132: University Physics Lab II (2017 Fall)-'
prefix2 = 'PHY 114: General Physics Laboratory (2017 Fall)-'
data = pd.read_csv(filename, dtype=str, delimiter=',', header=None)

"""Initialize WebDriver object"""
driver = webdriver.Chrome('/Users/smccaffrey/Desktop/LMSA-core/scripts/drivers/chromedriver_233')

"""Change to FALSE when ready to save changes"""
DRYRUN = True

"""Declare objects"""
institution = ASU_manipulator(driver)
PRELABS = Tests(driver)
LAB_REPORTS = Assignments(driver)
FORM = Editor(driver)

"""Login"""
institution.login()

"""Navigate home"""
Window(driver).home(wait=3)
time.sleep(4)

"""Bulk Edit"""
i = 1
for i in range(1, len(data[0])):

    """This pause is a quick fix for elementNotFound error"""
    pause = raw_input('Scroll until desired section is in view\n\nOnce in view press: <ENTER>')

    """This is the code that finds each section number on the BlackBoard homepage"""
    driver.find_element_by_link_text(prefix1 + str(data[0][i])).click()
    print('Starting Section: ' + str(data[0][i]))

    """Prelabs"""
    driver.find_element_by_link_text('PRELABS').click()
    j = 1
    for j in range(1, 11):
        FORM.select_form(data[j+4][0], wait=1)
        driver.find_element_by_xpath('//a[@title="Edit the Test Options"]').click()
        Tests(driver).due_date(state=True, date=data[j+4][i], time=data[3][i])
        #form.assignment_due_date(state=True, date=df1[j+4][i], time=df1[3][i])
        if not DRYRUN:
            FORM.submit(wait=2)
        FORM.cancel(wait=2)

    """Lab reports"""
    driver.find_element_by_link_text('Submit Lab Reports').click()
    k = 1
    for k in range(1, 11):
        FORM.select_form(data[k+14][0], wait=1)
        LAB_REPORTS.edit(wait=5)
        LAB_REPORTS.due_date(state=True, date=data[k+14][i], time=data[4][i])
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #quick fix for elementNotFound
        time.sleep(2)
        #form.folder_end_restrict_date(state=True, date=df1[k+14][i], time=df1[4][i])
        if not DRYRUN:
            FORM.submit(wait=2)
        FORM.cancel(wait=2)

    """Navigate Home"""
    Window(driver).home(wait=3)
    time.sleep(3)

import sys
import time
sys.path.append('/Users/smccaffrey/Desktop/LMSA-core/src/')
import pandas as pd
from lmsa.manipulation.ASU.ASU_manipulator import ASU_manipulator
from lmsa.lms.blackboard.BB_Editor import BB_Editor
from selenium import webdriver

from lmsa.manipulation.ASU.ASU_manipulator import ASU_manipulator
from lmsa.lms.blackboard.BlackBoard import Editor
from lmsa.lms.blackboard.content.tests import Tests as PRELABS
from lmsa.lms.blackboard.content.assignments import Assignments as LAB_REPORTS
from lmsa.lms.blackboard.content.folders import Folders
from lmsa.lms.blackboard.Library import Logic
from lmsa.lms.blackboard.Library import Window


filename = '/Users/smccaffrey/Desktop/PHY122_Fall2017_due_dates.csv'
p = 'PHY 122: University Physics Lab I (2017 Fall)-'
q = '2017Fall-T-PHY122-71848: PHY 122: University Physics Lab I (2017 Fall)'
df1 = pd.read_csv(filename, dtype=str, delimiter=',', header=None)
driver = webdriver.Chrome('/Users/smccaffrey/Projects/drivers/chromedriver')
BB_HOME = 'https://myasucourses.asu.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1'

"""Change when ready to save changes"""
DRYRUN = True

"""Declare objects"""
institution = ASU_manipulator(driver)
#form = BB_Editor(driver)
form = Editor(driver)

"""Login"""
institution.login()

Window(driver).home(wait=3)
time.sleep(4)

"""Bulk Edit"""
i = 1
for i in range(1, len(df1[0])):
    driver.find_element_by_link_text('2017Fall-T-PHY122-' + str(df1[0][i]) + ': PHY 122: University Physics Lab I (2017 Fall)').click()
    print('Starting Section: ' + str(df1[0][i]))

    """Prelabs"""
    driver.find_element_by_link_text('Submit PreLab').click()
    j = 1
    for j in range(1, 11):
        form.select_form(df1[j+4][0], wait=1)
        form.edit(wait=4)
        PRELABS.due_date(state=True, date=df1[j+4][i], time=df1[3][i])
        #form.assignment_due_date(state=True, date=df1[j+4][i], time=df1[3][i])
        if not DRYRUN:
            form.submit(wait=2)
        form.cancel(wait=2)

    """Lab reports"""
    driver.find_element_by_link_text('Submit Lab Report').click()
    k = 1
    for k in range(1, 11):
        form.select_form(df1[k+14][0], wait=1)
        form.edit(wait=5)
        LAB_REPORTS.due_date(state=True, date=df1[k+14][i], time=df1[4][i])
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #quick fix for elementNotFound
        time.sleep(2)
        #form.folder_end_restrict_date(state=True, date=df1[k+14][i], time=df1[4][i])
        if not DRYRUN:
            form.submit(wait=2)
        form.cancel(wait=2)

    """Navigate Home"""
    Window(driver).home(wait=3)
    time.sleep(3)

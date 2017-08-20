import sys
import time
sys.path.append('/Users/smccaffrey/Desktop/LMSA-core/src/')
import pandas as pd
from lmsa.manipulation.ASU.ASU_manipulator import ASU_manipulator
from lmsa.lms.blackboard.BB_Editor import BB_Editor
from selenium import webdriver

filename = '/Users/smccaffrey/Downloads/LMSA-core-ce8d77a2dcc81854e0502902fdde6a175acfe800/PHY122_Fall2017/duedates_Fall2017.csv'
p = 'PHY 122: University Physics Lab I (2017 Fall)-'
df1 = pd.read_csv(filename, dtype=str, delimiter=',', header=None)
driver = webdriver.Chrome('/Users/smccaffrey/Desktop/chromedriver')

"""Change when ready to save changes"""
DRYRUN = True

"""Declare objects"""
institution = ASU_manipulator(driver)
form = BB_Editor(driver)

"""Login"""
institution.login()

"""Bulk Edit"""
i = 1
for i in range(1, len(df1[0])):
    driver.find_element_by_link_text(p + str(df1[0][i])).click()

    """Prelabs"""
    driver.find_element_by_link_text('Submit PreLab').click()
    j = 1
    for j in range(1, 11):
        form.select_form(df1[j+4][0], wait=1)
        form.edit(wait=4)
        form.due_date(state=True, date=df1[j+4][i], time=df1[3][i])
        if not DRYRUN:
            form.submit(wait=2)
        form.cancel(wait=2)

    """Lab reports"""
    driver.find_element_by_link_text('Submit Lab Report').click()
    k = 1
    for k in range(1, 11):
        form.select_form(df1[k+14][0], wait=1)
        form.edit(wait=5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        form.end_restrict(state=True, date=df1[k+14][i], time=df1[4][i])
        if not DRYRUN:
            form.submit(wait=2)
        form.cancel(wait=2)

    """Navigate Home"""
    driver.get('https://myasucourses.asu.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_2_1')

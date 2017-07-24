import selenium
import getpass
import time
import sys
import pandas as pd

sys.path.append('/home/sysadmin/Projects/LMSA-core/src')
from selenium import webdriver as wbd
from selenium.webdriver.common.by import By

from lmsa.manipulator.ASU import ASU_manipulator
from lmsa import Editor as prelabs
from lmsa import assignment_options as lab_reports
from lmsa import SideBar
#from lmsa import authorization
from lmsa import SectionSelector



if __name__ == '__main__':

    """ --- Define Client variables --- """
    filename = '/home/sysadmin/Projects/LMSA-core/tests/client_builds/PHY132_Fall2017/PHY132_Fall2017_v2.csv'
    p = 'PHY 132: University Physics Lab II (2017 Fall)-'
    URL = 'https://myasucourses.asu.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1'

    """ --- Initiate Driver Object --- """
    driver = wbd.Chrome('/home/sysadmin/Projects/chromedriver')

    """ --- Login --- """
    ASU_manipulator(driver).login()

    """ --- Parse Due Date Data --- """
    df1 = pd.read_csv(filename, dtype=str, delimiter=',', header=None)


    """ --- Itereate through ALL Sections and update ALL Assignments --- """
    i = 1
    for i in range (1, len(df1[0])):
        SectionSelector(driver).find_section(module = p, section = df1[0][i], wait = 5)
        SideBar(driver).navigate_to(element = 'PRELABS', wait = 5)
        j = 1
        for n in range(1, 11):
            prelabs(driver).assignmentSelector(element = df1[n+2][0], wait = 5)
            print("Editing SECTION: " + str(df1[0][i]) + " " + df1[n+2][0])
            prelabs(driver).editTestOptions(wait = 3)
            prelabs(driver).startRestrictCheck(state = False)
            prelabs(driver).endRestrictCheck(state = False)
            prelabs(driver).dueDate(date = df1[n+2][i])
            prelabs(driver).dueDateTime(time = df1[1][i])
            prelabs(driver).dueDateCheck(state = True)
            """
            for x in range(0, 2):
                prelabs(d).dueDateCheck(state = True)
            for x in range(0, 2):
                prelabs(d).dueDateCheck(state = True)
            for x in range(0, 1):
                prelabs(d).lateSubmissionCheck(state = True)
            """
            pause = raw_input("Press <ENTER> to continue: ")
            if not dryrun:
                prelabs(driver).submit(wait = 7)
            prelabs(driver).cancel(wait = 7)

            driver.find_element_by_link_text(module2).click()
            time.sleep(3)

            for n in range(1, 10):
                lab_reports.assignmentSelector(driver = d, module = module2, assignment = df1[n+12][0])
                print("Editing SECTION: " + str(df1[0][i]) + " " + df1[n+12][0])
                time.sleep(5)
                lab_reports.edit_test_options(d)
                time.sleep(3)
                lab_reports.start_restrict(d, False)
                lab_reports.end_restrict(d, False)
                lab_reports._dueDate(d, True)
                lab_reports.dp_dueDate_date(d, df1[n+12][i])
                lab_reports.tp_dueDate_time(d, df1[2][i])
                #pause = raw_input("Press <ENTER> to continue: ")
                lab_reports.cancel(d)
            d.get(URL)
            time.sleep(4)

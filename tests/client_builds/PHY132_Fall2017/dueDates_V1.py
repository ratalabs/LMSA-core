import selenium
import getpass
import time
import sys
import logging as log
import pandas as pd
from selenium import webdriver as wbd
from selenium.webdriver.common.by import By

sys.path.append('/Users/smccaffrey/Desktop/BlackboardAssistant/')
from automation import test_options as prelabs
from automation import assignment_options as lab_reports
from automation import SideBar
from automation import authorization
from automation import SectionSelector


### Creates the browser instance in which all operations take place ###
#driver = wbd.Chrome('/Users/smccaffrey/Desktop/BlackboardAssistant/automation/lib/chromedriver2_26')
driver = wbd.Chrome()
filename = '/Users/smccaffrey/Desktop/BlackboardAssistant/tests/client_builds/PHY132_Fall2017/PHY132_Fall2017_v2.csv'
p = 'PHY 132: University Physics Lab II (2017 Fall)-'
URL = 'https://myasucourses.asu.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1'

### Parsers excel workbook (must be .csv file) ###
def parser(filename):
    df1 = pd.read_csv(filename, dtype=str, delimiter=',', header=None)
    return df1

### Update Prelabs information ###
def updater(d, p, URL, arr, module1, module2, dryrun=True):
    i = 1
    for i in range(1, len(arr[0])):
        SectionSelector(d).find_section(module = p, section = arr[0][i], wait = 5)
        #d.find_element_by_link_text(p + str(arr[0][i])).click()
        time.sleep(5)
        SideBar(d).navigate_to(element = 'PRELABS', wait = 5)
        #d.find_element_by_link_text(module1).click()
        #time.sleep(5)

        n = 1
        for n in range (1, 11):
            prelabs.assignmentSelector(driver = d, module = module1, test = arr[n+2][0], index = n)
            print("Editing SECTION: " + str(arr[0][i]) + " " + arr[n+2][0])
            time.sleep(5)
            prelabs.edit_test_options(d)
            time.sleep(3)
            prelabs.start_restrict(d, False)
            prelabs.end_restrict(d, False)
            prelabs.dp_dueDate_date(d, arr[n+2][i])
            prelabs.tp_dueDate_time(d, arr[1][i])

            for x in range(0, 2):
                prelabs._dueDate(d, True)
            for x in range(0, 2):
                prelabs._dueDate(d, True)
            for x in range(0, 1):
                prelabs._lateSubmission(d, True)

            #pause = raw_input("Press <ENTER> to continue: ")
            if not dryrun:
                prelabs.submit(d)
            prelabs.cancel(d)

            time.sleep(7)

        d.find_element_by_link_text(module2).click()
        time.sleep(3)

        for n in range(1, 10):
            lab_reports.assignmentSelector(driver = d, module = module2, assignment = arr[n+12][0])
            print("Editing SECTION: " + str(arr[0][i]) + " " + arr[n+12][0])
            time.sleep(5)
            lab_reports.edit_test_options(d)
            time.sleep(3)
            lab_reports.start_restrict(d, False)
            lab_reports.end_restrict(d, False)
            lab_reports._dueDate(d, True)
            lab_reports.dp_dueDate_date(d, arr[n+12][i])
            lab_reports.tp_dueDate_time(d, arr[2][i])
            #pause = raw_input("Press <ENTER> to continue: ")
            lab_reports.cancel(d)
        d.get(URL)
        time.sleep(4)

### test function ###
def test_func(d, filename, dryrun=False):
    parser(filename)
    if not dryrun:
        authorization.login(driver = d, url = URL, wait = 10)
        authorization.dual_factor(driver = d, wait = 14)
        updater(d, p, URL, parser(filename), module1 = 'PRELABS', module2 = 'Submit Lab Reports')

if __name__ == '__main__':
   test_func(driver, filename)

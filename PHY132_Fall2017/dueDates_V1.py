import selenium
import getpass
import time
import sys
import logging as log
import pandas as pd
from selenium import webdriver as wbd
from selenium.webdriver.common.by import By

sys.path.append('/Users/smccaffrey/Desktop/blackboard_automation/')
from blackboard_automation import tests as prelabs
from blackboard_automation import assignments as lab_reports

### Creates the browser instance in which all operations take place ###
driver = wbd.Chrome('/Users/smccaffrey/Desktop/blackboard_automation/lib/chromedriver2.26')
filename = '/Users/smccaffrey/Desktop/blackboard_automation/PHY132_Fall2017/PHY132_Fall2017.csv'
p = 'PHY 132: University Physics Lab II (2017 Fall)-'
URL = 'https://myasucourses.asu.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1'

### Parsers excel workbook (must be .csv file) ###
def parser(filename):
    df1 = pd.read_csv(filename, dtype=object, delimiter=',', header=None)
    return df1

### Authenticates MyASU credentials ###
def authorization(d, URL, username=None, t=15):
    if not username:
        username = raw_input("Enter ASURITE username: ")
    password = getpass.getpass("Enter ASURITE password: ")

    #URL = 'https://myasucourses.asu.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1'

    d.get(URL)
    d.find_element_by_id("username").send_keys(username)
    d.find_element_by_id("password").send_keys(password)
    d.find_element_by_class_name('submit').click()

    time.sleep(t) #Gives you time for 2-Step Authentication

### Update Prelabs information ###
def updater(d, p, URL, arr, module1, module2, dryrun=True):
    i = 1
    for i in range(1, len(arr[0])):
        time.sleep(5)
        d.find_element_by_link_text(p + str(arr[0][i])).click()
        time.sleep(5)
        d.find_element_by_link_text(module1).click()
        time.sleep(5)
        n = 1

        #log.basicConfig(format = '%(message)s', filename='Desktop/DueDates.log')
        #log.info('SECTION: ' + arr[0][i] + '\n')

        #len(arr.columns)
        for n in range (1, 10):
            prelabs.assignmentSelector(driver = d, module = module1, test = arr[n+2][0])
            print(arr[n+2][0])
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

            pause = raw_input("Press <ENTER> to continue: ")
            if not dryrun:
                prelabs.submit(d)
            prelabs.cancel(d)
            time.sleep(7)

        d.find_element_by_link_text(module2).click()
        time.sleep(3)

        for n in range(1, 10):
            lab_reports.assignmentSelector(driver = d, module = module2, assignment = arr[n+12][0])
            time.sleep(5)
            lab_reports.edit_test_options(d)
            time.sleep(3)
            lab_reports.start_restrict(d, False)
            lab_reports.end_restrict(d, False)
            lab_reports._dueDate(d, True)
            lab_reports.dp_dueDate_date(d, arr[n+12][i])
            lab_reports.tp_dueDate_time(d, arr[2][i])
            pause = raw_input("Press <ENTER> to continue: ")
            lab_reports.cancel(d)
        d.get(URL)

### test function ###
def test_func(d, filename, dryrun=False):
    parser(filename)
    if not dryrun:
        authorization(d, URL)
        updater(d, p, URL, parser(filename), module1 = 'PRELABS', module2 = 'Submit Lab Reports')
test_func(driver, filename)

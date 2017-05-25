import selenium
import getpass
import time
import pandas as pd
from selenium import webdriver as wbd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from blackboard_automation import tests as prelabs

### Creates the browser instance in which all operations take place ###
driver = wbd.Chrome('/Users/smccaffrey/Desktop/git/PIRT_ASU/lib/chromedriver')
filename = '/Users/smccaffrey/Desktop/git/PIRT_ASU/PHY132_Fall2017.csv'

p = 'PHY 132: University Physics Lab II (2017 Fall)-'

URL = 'https://myasucourses.asu.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1'


### Parsers excel workbook (must be .csv file) ###
def parser(filename):
    df1 = pd.read_csv(filename, dtype=object, delimiter='\t', header=None)
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
def updater(d, p, URL, arr, module, dryrun=True):
    i = 1
    for i in range(1, len(arr[0])):
        time.sleep(5)
        d.find_element_by_link_text(p + str(arr[0][i])).click()
        time.sleep(5)
        d.find_element_by_link_text(module).click()
        time.sleep(5)
        n = 1
        for n in range (1, len(arr.columns)-13):
            prelabs.assignmentSelector(driver = d, module = module, test = arr[n+2][0])
            time.sleep(5)
            prelabs.edit_test_options(d)
            time.sleep(3)
            prelabs.start_restrict(d, False)
            prelabs.end_restrict(d, False)
            prelabs._dueDate(d, True)
            prelabs.dp_dueDate_date(d, arr[n+2][i])
            prelabs.tp_dueDate_time(d, arr[1][i])
            prelabs._lateSubmission(d, True)
            pause = raw_input("Press <ENTER> to continue: ")
            prelabs.cancel(d)
            time.sleep(7)
        d.get(URL)

### test function ###
def test_func(d, filename, dryrun=False):
    parser(filename)
    if not dryrun:
        authorization(d, URL)
        updater(d, p, URL, parser(filename), module = 'PRELABS')

test_func(driver, filename)

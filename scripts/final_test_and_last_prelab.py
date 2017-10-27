import sys, time
import pandas as pd
from selenium import webdriver
sys.path.append('/Users/smccaffrey/Desktop/LMSA-core/src/')

"""Import functionality for navigating and logging into ASU
"""
from lmsa.manipulation.ASU.ASU_manipulator import ASU_manipulator

"""Import the main BlackBoard Editor
"""
from lmsa.lms.blackboard.BlackBoard import Editor

"""Import all the content editing modules
"""
from lmsa.lms.blackboard.content.tests import Tests
from lmsa.lms.blackboard.content.assignments import Assignments
from lmsa.lms.blackboard.content.folders import Folders

"""Import Logic operations, general window manipulations
"""
from lmsa.lms.blackboard.Library import Logic
from lmsa.lms.blackboard.Library import Window
#Window(driver).home()

"""Global Variables
"""
FILENAME = "/Users/smccaffrey/Desktop/PHY132Fall2017_FinalEdit.csv"
df1 = pd.read_csv(FILENAME, dtype=str, delimiter=',', header=None)
driver = webdriver.Chrome('/Users/smccaffrey/Projects/drivers/chromedriver')
DRYRUN = True

"""ASU institution declaration
"""
institution = ASU_manipulator(driver)
form = Editor(driver)

if (__name__ == '__main__' and DRYRUN == False):
    institution.login()

    """Bulk Edit"""

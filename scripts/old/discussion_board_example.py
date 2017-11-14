import sys
import time
sys.path.append('/Users/smccaffrey/Desktop/LMSA-core/src/')
import pandas as pd
from selenium import webdriver

from lmsa.manipulation.ASU.ASU_manipulator import ASU_manipulator
from lmsa.lms.blackboard.BlackBoard import Editor
from lmsa.lms.blackboard.content.tests import Tests
from lmsa.lms.blackboard.content.assignments import Assignments
from lmsa.lms.blackboard.content.folders import Folders
from lmsa.lms.blackboard.Library import Logic
from lmsa.lms.blackboard.Library import Window

"""Change when ready to save changes"""
DRYRUN = True

"""
filename = '/Users/smccaffrey/Desktop/PHY122_Fall2017_due_dates.csv'
p = 'PHY 122: University Physics Lab I (2017 Fall)-'
q = '2017Fall-T-PHY122-71848: PHY 122: University Physics Lab I (2017 Fall)'
df1 = pd.read_csv(filename, dtype=str, delimiter=',', header=None)
driver = webdriver.Chrome('/Users/smccaffrey/Projects/drivers/chromedriver')
BB_HOME = 'https://myasucourses.asu.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1'
"""

"""Declare objects"""
institution = ASU_manipulator(driver)
form = BB_Editor(driver)

"""Cycle through Discussion Board Threads"""
# Select Group
    # Select Thread
        # Harvest Post
        # Harvest All Replies
        # Time Stamp
        # Record Author
        # Record any other relevent information
    # Back to thread page
    # Next Thread, rr
    # .
    # .
    # .
    # Next Group (Team)

### Maybe save Each Team for a section to separte files

import sys
sys.path.append('/Users/smccaffrey/Desktop/LMSA-core/src/')

from lmsa.manipulation.ASU.ASU_manipulator import ASU_manipulator
from lmsa.lms.blackboard.BB_Editor import BB_Editor
from selenium import webdriver

driver = webdriver.Chrome('/Users/smccaffrey/Desktop/chromedriver')

institution = ASU_manipulator(driver)
institution.login()

"""Interact with a specific field in web form"""
test_element = 'Prelab: Magnetic Fields'
course = BB_Editor(driver)
course.select_form(test_element)

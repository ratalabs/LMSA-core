from lmsa.manipulator.ASU import ASU_manipulator
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path="/home/ikenney/Library/webdrivers/phantomjs/2.1.1/bin/phantomjs")
manip = ASU_manipulator(driver)

manip.login()
manip.nav_courses()
manip.get_instructor_course_list()
print(manip.courses)

driver.close()

from lmsa.manipulation.ASU.ASU_manipulator import ASU_manipulator
from selenium import webdriver

#driver = webdriver.PhantomJS(executable_path="/home/ikenney/Library/webdrivers/phantomjs/2.1.1/bin/phantomjs")
driver = webdriver.Chrome(executable_path="/home/ikenney/Library/webdrivers/chrome/chromedriver")
manip = ASU_manipulator(driver)

manip.login()
manip.scan_courses()
for c in manip.lms.courses.keys():
    course = manip.lms.courses[c]
    print(course.sections)

driver.close()

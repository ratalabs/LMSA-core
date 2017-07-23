from lmsa.manipulator.ASU import ASU_manipulator
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/ikenney/Library/webdrivers/chrome/chromedriver")
manip = ASU_manipulator(driver)

manip.login()
driver.close()

from lmsa.authentication.Duo import Duo
from lmsa.manipulator import Manipulator
import lmsa.lms.blackboard
import time

import getpass

class ASU_manipulator(Manipulator):

    URLS = {'LOGIN':r'https://my.asu.edu',
            'COURSE_LIST':r'https://myasucourses.asu.edu',
            'WEBAPPS':r'https://myasucourses.asu.edu/webapps/'}

    AUTHENTICATION_CLASS = Duo
    LMS_CLASS = lmsa.lms.blackboard.BlackBoard


    def __init__(self, driver):
        self.driver = driver
        self.authenticator = ASU_manipulator.AUTHENTICATION_CLASS(self.driver)
        self.lms = ASU_manipulator.LMS_CLASS(self.driver, ASU_manipulator)

    def __gather_login_raw__(self):
        uname = raw_input("Enter ASURITE username: ")
        pword = getpass.getpass("Enter ASURITE password: ")
        self.driver.find_element_by_id('username').send_keys(uname)
        self.driver.find_element_by_id('password').send_keys(pword)
        self.driver.find_element_by_class_name('submit').click()

    def login(self):
        self.driver.get(ASU_manipulator.URLS['LOGIN'])
        self.__gather_login_raw__()
        self.authenticator.authenticate()

    def scan_courses(self):
        self.lms.nav_courses()
        self.lms.get_instructor_course_list()

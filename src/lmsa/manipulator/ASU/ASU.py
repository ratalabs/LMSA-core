from lmsa.authentication.Duo import Duo
from lmsa.manipulator import Manipulator
import time

import getpass

class ASU_manipulator(Manipulator):

    LOGIN_PAGE = r'https://weblogin.asu.edu/cas/login?service=https%3A%2F%2Fweblogin.asu.edu%2Fcgi-bin%2Fcas-login%3Fcallapp%3Dhttps%253A%252F%252Fwebapp4.asu.edu%252Fmyasu%252F%253Finit%253Dfalse'
    COURSE_LIST_URL = r'https://myasucourses.asu.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_2_1'
    AUTHENTICATION_CLASS = Duo

    def __init__(self, driver):
        super(ASU_manipulator, self).__init__()
        self.driver = driver
        self.authenticator = ASU_manipulator.AUTHENTICATION_CLASS(self.driver)

    def __gather_login_raw__(self):
        uname = raw_input("Enter ASURITE username: ")
        pword = getpass.getpass("Enter ASURITE password: ")
        self.driver.find_element_by_id('username').send_keys(uname)
        self.driver.find_element_by_id('password').send_keys(pword)
        self.driver.find_element_by_class_name('submit').click()

    def login(self):
        self.driver.get(ASU_manipulator.LOGIN_PAGE)
        self.__gather_login_raw__()
        self.authenticator.authenticate()

    def nav_courses(self):
        self.driver.get(ASU_manipulator.COURSE_LIST_URL)
        self.driver.find_element_by_id('anonymous_element_14')

    def get_instructor_course_list(self):
        self.courses = super(ASU_manipulator, self).get_instructor_course_list()

from bs4 import BeautifulSoup
from urlparse import urljoin
import time


from lmsa.lms.LMS import LMS
from .Course import Course
from .content.tests import Tests
from .content.assignments import Assignments
from .content.folders import Folders

class BlackBoard(LMS):

    XPATHS = dict()

    def __init__(self, driver, institute):
        super(BlackBoard, self).__init__(driver)
        self.institute = institute
        self.courses = dict()

    def nav_courses(self):
        """Navigate to course list.
        """
        self.driver.get(self.institute.URLS['COURSE_LIST'])
        time.sleep(2)
        self.driver.find_element_by_id('anonymous_element_14')

    def parse_course_info(self, anchor):
        """Reads in an anchor containing an href to course page
        and returns a tuple of that courses information.

        Parameters
        ----------
        anchor : str
            Raw html of the anchor containing the course information.

        current_url : str
            Since the anchor href does not contain the first portion
            of the destination, we need to construct it within the
            function. The current url contains the initial part of the
            link.

        Returns
        -------
        (str, str, str)
                Tuple containing the name of the course as seen on BlackBoard,
                the url to the course, and the course id.

        """
        href = anchor['href']
        new_url = urljoin(self.institute.URLS['COURSE_LIST'], href.strip())
        #new_url = current_url.split('webapps')[0][:-1] + href.strip()
        options = href.split('?')[1]
        sep_options = options.split('&')[1]
        return anchor.text.strip(), new_url, sep_options.split('=')[1], self.institute

    def get_instructor_course_list(self):
        """When used while on a page containing the course list, this function
        returns a list of the courses in tuple form.

        Returns
        -------
        [(str,str,str)]
            List of tuples containing the name of the courses as seen on
            Blackboard, the urls to the courses, and the course ids.
        """
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        courses = soup.find_all('ul', {'class':['portletList-img',
                                                'courseListing',
                                                'coursefakeclass']})
        for x in courses[0].find_all('li'):
            anchor = x.find('a')
            parsed = self.parse_course_info(anchor)
            self.courses[parsed[2]] = Course(*parsed)
        for c in self.courses.keys():
            course = self.courses[c]
            self.driver.get(course.url)
            self.driver.find_element_by_id('courseMenuPalette_contents')
            course.gather_sections(self.driver.page_source)

class Editor(Tests, Assignments, Folders):

    def __init__ (self, driver):
        seld.driver = driver

    CANCEL = '//*[@id="bottom_submitButtonRow"]/input[1]'
    SUBMIT = '//*[@id="bottom_submitButtonRow"]/input[2]'

    def select_form(self, element, wait=None):
        """Selects the options dropdown menu for blackboard
        form items.

        Parameters
        ----------
        element : str
            User inputed title of form name

        wait : int
            Time to pause for page load to complete. Default is None

        Returns
        -------
        """
        self.driver.find_element_by_xpath('//a[@title=' + "\"" + element + " item options" + "\"" ']').click()
        print('     Editing: ' + element)
        if wait is not None:
            time.sleep(wait)

    def edit(self, wait=None):
        self.driver.find_element_by_xpath('//a[@title="Edit"]').click()
        if wait is not None:
            time.sleep(wait)

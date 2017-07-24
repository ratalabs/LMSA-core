from lmsa.lms import LMS
from bs4 import BeautifulSoup
import time

class BlackBoard(LMS):

    URLS = {'COURSE_LIST':r'https://myasucourses.asu.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_2_1'}
    XPATHS = {'':''}

    def nav_courses(self):
        """Navigate to course list.
        """
        self.driver.get(BlackBoard.URLS['COURSE_LIST'])
        time.sleep(2)
        self.driver.find_element_by_id('anonymous_element_14')

    def parse_course_info(self, anchor, current_url):
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
        new_url = current_url.split('webapps')[0][:-1] + href.strip()
        options = href.split('?')[1]
        sep_options = options.split('&')[1]
        return anchor.text.strip(), new_url, sep_options.split('=')[1]

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
        results = []
        current_url = self.driver.current_url
        for x in courses[0].find_all('li'):
            anchor = x.find('a')
            results.append(self.parse_course_info(anchor, current_url))
        self.course_list = results
        return results

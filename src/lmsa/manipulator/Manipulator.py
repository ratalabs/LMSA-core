from bs4 import BeautifulSoup

class Manipulator(object):

    def parse_course_info(self, cl, current_url):
        anchor = cl.find('a')
        href = anchor['href']
        new_url = current_url.split('webapps')[0][:-1] + href.strip()
        options = href.split('?')[1]
        sep_options = options.split('&')[1]
        return anchor.text.strip(), new_url, sep_options.split('=')[1]

    def get_instructor_course_list(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        courses = soup.find_all("ul", {"class":["portletList-img",
                                                "courseListing",
                                                "coursefakeclass"]})
        result = []
        for x in courses[0].find_all("li"):
            result.append(self.parse_course_info(x, self.driver.current_url))
        self.course_list = result
        return result

from lmsa.lms.blackboard.Section import Section
import bs4
from urlparse import urljoin

class Course(object):

    def __init__(self, name, url, course_id, institute):
        self.sections = dict()
        self.name = name
        self.url = url
        self.course_id = course_id
        self.institute = institute

    def gather_sections(self, html):
        soup = bs4.BeautifulSoup(html, 'html.parser')
        palette = soup.find('ul',{'id':'courseMenuPalette_contents'})
        course_list = palette.find_all('li')
        section_names = [c.find('a').find('span').text for c in course_list]
        section_urls = [urljoin(self.institute.URLS['COURSE_LIST'], c.find('a')['href']) for c in course_list]
        sections = [Section(*x) for x in zip(section_names,section_urls)]
        self.sections.update(dict(zip(section_names,sections)))

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

"""
Handles any editing operations/logic unique to the Blackboard LMS
"""

#from lmsa.lms.blackboard.options import assignment_options
#from lmsa.lms.blackboard.options import test_options

import time

class Editor(object):

    CANCEL = '//*[@id="bottom_submitButtonRow"]/input[1]'
    SUBMIT = '//*[@id="bottom_submitButtonRow"]/input[2]'

    def __init__(self, driver):
        self.driver = driver

    def home(self, wait=None):
        self.driver.get('https://myasucourses.asu.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1')
        if wait is not None:
            time.sleep(wait)

    def scroll_page_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    def scroll_into_view(self):
        #item = self.driver.find_element_by_xpath
        #self.driver.execute_script("%s.scrollIntoView(true);" % document.getElementById("due_date_in_use"))
        elementID = 'due_date_in_use'
        #//*[@id="newFile_chooseLocalFile"]
        self.driver.execute_script("document.getElementById('newFile_chooseLocalFile').scrollIntoView(true);")

    def maximize_window(self):
        self.driver.maximize_window()

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

    def check_state(self, xpath):
        """Checks the state of a given element, returns
        its boolean value.

        Parameters
        ----------
        xpath : str
            Raw xpath formatted as string value. Should be using
            global variable from assignment_options/test_options

        Returns
        -------
        boolean
            Returns 'True' if element is selected, and 'False' otherwise
        """
        x = self.driver.find_element_by_xpath(xpath)
        if x.is_selected() == True:
            return True
        return False

    def set_state(self, xpath, dstate):
        """Sets the desired state of an element.

        Parameters
        ----------
        xpath : str
            Raw xpath formatted as string value. Should be using
            global variable from assignment_options/test_options

        state : bool
            The user's desired state for the given element

        Returns
        -------
        """
        if self.check_state(xpath) != dstate:
            self.driver.find_element_by_xpath(xpath).click()

    def open_test_new_windows(self):
        """Open test in a new (pop-up) windows (YES/NO)
        """
        return

    def make_link_available(self):
        """Toggle if the content link is available to users/students
        """
        return

    def create_announcement(self):
        """Toggle the creation of an announcement upon editing content
        """
        return

    def late_submission(self):
        """Choose whether to allow late submissions
        """
        return

    def test_start_restrict_date(self):
        """Edit starting restrict date and time for test content
        """
        return

    def test_end_restrict_date(self):
        """Edit ending restrict date and time for test content
        """
        return

    def assignment_start_limit_availability(self):
        """Editing starting availablilty date and time for assignment content
        """
        return

    def assignment_end_limit_availability(self):
        """Editing ending availablilty date and time for assignment content
        """
        return

    def folder_start_restrict_date(self, state, date, time):
        """Performs all operations related to the 'Start Restrict Date'. Order matters when invoking multiple
        'send_key' functions.

        Parameters
        ----------
        state : bool
            The desired state of the checkbox element (True/False)

        date : str
            The literal date value in the format mm/dd/yyyy

        time : str
            The literal time value in the format hh:mm AM/PM

        Returns
        -------
        """
        current_state = self.check_state(folder_options.START_RESTRICT_CHECK)
        if current_state != state:
            self.set_state(xpath=folder_options.START_RESTRICT_CHECK, dstate=state)
        if state:
            self.driver.find_element_by_xpath(folder_options.START_RESTRICT_DATE).clear()
            self.driver.find_element_by_xpath(folder_options.START_RESTRICT_TIME).clear()
            self.driver.find_element_by_xpath(folder_options.START_RESTRICT_TIME).send_keys(time)
            self.driver.find_element_by_xpath(folder_options.START_RESTRICT_DATE).send_keys(date)
        return

    def folder_end_restrict_date(self, state, date, time):
        """Performs all operations related to the 'End Restrict Date'. Order matters when invoking multiple
        'send_key' functions.

        Parameters
        ----------
        state : bool
            The desired state of the checkbox element (True/False)

        date : str
            The literal date value in the format mm/dd/yyyy

        time : str
            The literal time value in the format hh:mm AM/PM

        Returns
        -------
        """
        current_state = self.check_state(folder_options.END_RESTRICT_CHECK)
        if current_state != state:
            self.set_state(xpath=folder_options.END_RESTRICT_CHECK, dstate=state)
        if state:
            self.driver.find_element_by_xpath(folder_options.END_RESTRICT_DATE).clear()
            self.driver.find_element_by_xpath(folder_options.END_RESTRICT_TIME).clear()
            self.driver.find_element_by_xpath(folder_options.END_RESTRICT_TIME).send_keys(time)
            self.driver.find_element_by_xpath(folder_options.END_RESTRICT_DATE).send_keys(date)


    def assignment_due_date(self, state, date, time):
        """Performs all operations related to Due Dates. Order matters when invoking multiple
        'send_key' functions.

        Parameters
        ----------
        state : bool
            The desired state of the checkbox element (True/False)

        date : str
            The literal date value in the format mm/dd/yyyy

        time : str
            The literal time value in the format hh:mm AM/PM

        Returns
        -------
        """
        current_state = self.check_state(assignment_options.DUE_DATE_CHECK)
        if current_state != state:
            self.set_state(xpath=assignment_options.DUE_DATE_CHECK, dstate=state)
        if state:
            self.driver.find_element_by_xpath(assignment_options.DUE_DATE_VALUE).clear()
            self.driver.find_element_by_xpath(assignment_options.DUE_DATE_TIME).clear()
            self.driver.find_element_by_xpath(assignment_options.DUE_DATE_TIME).send_keys(time)
            self.driver.find_element_by_xpath(assignment_options.DUE_DATE_VALUE).send_keys(date)


    def multiple_attempts(self):
        """Edit multiple attempt field. Toggle YES/NO button, allow infinite submissions,
        and/or specify number of attempts
        """
        return

    def force_completion(self):
        """Force test completion if due date and time passed while student is taking test
        """
        return

    def cancel(self, wait=None):
        """Click cancel
        """
        try:
            self.driver.find_element_by_xpath(BB_Editor.CANCEL).click()
            if wait is not None:
                time.sleep(wait)
        except:
            return False

    def submit(self, wait=None):
        """Click submit
        """
        try:
            self.driver.find_element_by_xpath(BB_Editor.SUBMIT).click()
            if wait is not None:
                time.sleep(wait)
        except:
            return False

class test_options:

    OPEN_TEST_IN_NEW_WINDOW_YES = '//*[@id="yesRadio"]'
    OPEN_TEST_IN_NEW_WINDOW_NO = '//*[@id="noRadio"]'
    MAKE_LINK_AVAILABLE_YES = '//*[@id="fIsLinkVisible1"]'
    MAKE_LINK_AVAILABLE_NO = '//*[@id="fIsLinkVisible2"]'
    CREATE_ANNOUNCEMENT_YES = '//*[@id="fCreateAnnouncement1"]'
    CREATE_ANNOUNCEMENT_NO = '//*[@id="fCreateAnnouncement2"]'
    MULTIPLE_ATTEMPTS_CHECK = '//*[@id="fIsMultipleAttempts"]'
    ALLOW_UNLIMITED_ATTEMPTS = '//*[@id="fIsUnlimitedAttempts"]'
    NUMBER_OF_ATTEMPTS = '//*[@id="fNumMultipleAttempts"]'
    NUMBER_OF_ATTEMPTS_VALUE = '//*[@id="attemptCount"]'
    FORCE_COMPLETION_CHECK = '//*[@id="fIsForceComplete"]'
    START_RESTRICT_CHECK = '//*[@id="start_restrict"]'
    START_RESTRICT_DATE = '//*[@id="dp_restrict_start_date"]'
    START_RESTRICT_TIME = '//*[@id="tp_restrict_start_time"]'
    END_RESTRICT_CHECK = '//*[@id="end_restrict"]'
    END_RESTRICT_DATE = '//*[@id="dp_restrict_end_date"]'
    END_RESTRICT_TIME = '//*[@id="tp_restrict_end_time"]'
    DUE_DATE_CHECK = '//*[@id="_dueDate"]'
    DUE_DATE_DATE = '//*[@id="dp_dueDate_date"]'
    DUE_DATE_TIME = '//*[@id="tp_dueDate_time"]'
    LATE_SUBMISSION_CHECK = '//*[@id="doNotAllowLateSubmission"]'

class assignment_options:

    DUE_DATE_CHECK = '//*[@id="due_date_in_use"]'
    DUE_DATE_VALUE = '//*[@id="dp_dueDate_date"]'
    DUE_DATE_TIME = '//*[@id="tp_dueDate_time"]'
    POINTS_POSSIBLE = '//*[@id="possible"]'
    MAKE_ASSIGNMENT_AVAILABLE = '//*[@id="isAvailable"]'
    START_LIMIT_AVAILABILITY = '//*[@id="start_limitAvailability"]'
    START_LIMIT_AVAILABILITY_DATE = '//*[@id="dp_limitAvailability_start_date"]'
    START_LIMIT_AVAILABILITY_TIME = '//*[@id="tp_limitAvailability_start_time"]'
    END_LIMIT_AVAILABILITY = '//*[@id="end_limitAvailability"]'
    END_LIMIT_AVAILABILITY_DATE = '//*[@id="dp_limitAvailability_end_date"]'
    END_LIMIT_AVAILABILITY_TIME = '//*[@id="tp_limitAvailability_end_time"]'
    TRACK_NUMBER_OF_VIEWS_CHECK = '//*[@id="isTracked"]'

class folder_options:

    CONTENT_VIEW_ICON_ONLY = '//*[@id="iconOnlyView"]'
    CONTENT_VIEW_TEXT_ONLY = '//*[@id="textOnlyView"]'
    CONTENT_VIEW_ICON_AND_TEXT = '//*[@id="iconAndTextView"]'
    PERMIT_USERS_TO_VIEW_THIS_CONTENT_YES = '//*[@id="availableYes"]'
    PERMIT_USERS_TO_VIEW_THIS_CONTENT_NO = '//*[@id="availableNo"]'
    TRACK_NUMBER_OF_VIEWS_YES = '//*[@id="trackYes"]'
    TRACK_NUMBER_OF_VIEWS_NO = '//*[@id="trackNo"]'
    START_RESTRICT_CHECK = '//*[@id="start_bbDateTimePicker"]'
    START_RESTRICT_DATE = '//*[@id="dp_bbDateTimePicker_start_date"]'
    START_RESTRICT_TIME = '//*[@id="tp_bbDateTimePicker_start_time"]'
    END_RESTRICT_CHECK = '//input[@id="end_bbDateTimePicker"]'
    END_RESTRICT_DATE = '//*[@id="dp_bbDateTimePicker_end_date"]'
    END_RESTRICT_TIME = '//*[@id="tp_bbDateTimePicker_end_time"]'

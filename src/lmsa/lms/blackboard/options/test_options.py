"""
Stores all full XPATHS relating to edit test options.
"""

class test_options:

    OPEN_TEST_IN_NEW_WINDOW_YES = '//*[@id="yesRadio"]',
    OPEN_TEST_IN_NEW_WINDOW_NO = '//*[@id="noRadio"]',
    MAKE_LINK_AVAILABLE_YES = '//*[@id="fIsLinkVisible1"]',
    MAKE_LINK_AVAILABLE_NO = '//*[@id="fIsLinkVisible2"]',
    CREATE_ANNOUNCEMENT_YES = '//*[@id="fCreateAnnouncement1"]',
    CREATE_ANNOUNCEMENT_NO = '//*[@id="fCreateAnnouncement2"]',
    MULTIPLE_ATTEMPTS_CHECK = '//*[@id="fIsMultipleAttempts"]',
    ALLOW_UNLIMITED_ATTEMPTS = '//*[@id="fIsUnlimitedAttempts"]',
    NUMBER_OF_ATTEMPTS = '//*[@id="fNumMultipleAttempts"]',
    NUMBER_OF_ATTEMPTS_VALUE = '//*[@id="attemptCount"]',
    FORCE_COMPLETION_CHECK = '//*[@id="fIsForceComplete"]',
    START_RESTRICT_CHECK = '//*[@id="start_restrict"]',
    START_RESTRICT_DATE = '//*[@id="dp_restrict_start_date"]',
    START_RESTRICT_TIME = '//*[@id="tp_restrict_start_time"]',
    END_RESTRICT_CHECK = '//*[@id="end_restrict"]',
    END_RESTRICT_DATE = '//*[@id="dp_restrict_end_date"]',
    END_RESTRICT_TIME = '//*[@id="tp_restrict_end_time"]',
    DUE_DATE_CHECK = '//*[@id="_dueDate"]',
    DUE_DATE_DATE = '//*[@id="dp_dueDate_date"]',
    DUE_DATE_TIME = '//*[@id="tp_dueDate_time"]',
    LATE_SUBMISSION_CHECK = '//*[@id="doNotAllowLateSubmission"]'

"""
Stores all full XPATHS relating to editing 'Folder' options.
"""


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

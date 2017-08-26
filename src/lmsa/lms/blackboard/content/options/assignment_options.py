"""
Stores all full XPATHS relating to edit assignment options.
"""

#Need to map 'Submission Details' section
#Need to map 'Grading Options' section
#Need to map 'Display of Grades' section
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

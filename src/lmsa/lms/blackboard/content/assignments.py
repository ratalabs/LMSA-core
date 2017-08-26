"""
Handles any functionality related to editing 'Assignment' content items in
Blackboard
"""

from .options import assignment_options
from ..Library import Logic


class Assignments(object):

    def __init__ (self, driver):
        self.driver = driver

    def due_date(self):
        return

    def points_possible(self):
        return

    def start_limit_availability(self):
        return

    def end_limit_availability(self):
        return

    def track_number_of_views(self):
        return

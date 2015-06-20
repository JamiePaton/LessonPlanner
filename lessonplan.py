# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 14:43:50 2015

@author: Jamie
"""
TITLE = 'lessonplan'
VERSION = '0.0.1'
AUTHOR = 'Jamie E Paton'
TEST = 0

import sys
import logging
import unittest
import hypothesis as hs

import datetime as dt

from atom.api import Atom, Unicode, Range, Bool, observe, Value

import enaml
from enaml.qt.qt_application import QtApplication

from jsonobject import JSONObject

class EnamlLessonPlan(Atom, JSONObject):
    """
    Attributes
    ----------
    key_stage : int
        the key stage the lesson is aimed at, e.g. KS3
    
    subject : str
        the subject, e.g physics, chemistry, or biology
    
    Methods
    -------
    
    
    Notes
    -----
    
    """
#    def __init__(self):
#        self.key_stage
#        self.subject
#        self.specification_point
#        self.national_curriculum_link
#        self.previous_lesson_link
#        self.topic
#        self.title
#        self.subtitle
#        
#        self.sequence_id
#        self.learning_objectives
#        self.activities
#        self.homework
#        self.key_terms
#        self.resources
#        
#        self.group
#        self.date
#        self.time
        
        
    key_stage = Range(low=0)
    subject = Unicode()
    specification_point = Unicode()
    national_curriculum_link = Unicode()
    previous_lesson_link = Unicode()
    topic = Unicode()
    title = Unicode()
    subtitle = Unicode()
    
    sequence_id = Unicode()
    learning_objectives = Unicode()
    activities = Unicode()
    homework = Unicode()
    key_terms = Unicode()
    resources = Unicode()
    group = Unicode()
    date = Value(dt.date.today())
    time = Unicode()
    
    @observe('key_stage')
    def print_self(self, change):
        print self

def main(args):
    with enaml.imports():
        from lesson_view import LessonPlanView
    
    lesson = LessonPlan(key_stage=2)
    app = QtApplication()
    view = LessonPlanView(lessonplan=lesson)
    view.show()
    print lesson
    app.start()
    
class Testing(unittest.TestCase):
    """
    
    Methods
    -------
    
    
    Notes
    -----
    @given(parameter=hs.strategies.integers())
    
    def test_something(parameter):
        assert type(parameter) == int
    """


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info(''.join([TITLE, ' v', VERSION, ' ', AUTHOR]))
    sys.exit(main(sys.argv))


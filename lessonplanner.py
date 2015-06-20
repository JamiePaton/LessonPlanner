# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 17:22:40 2015

@author: Jamie
"""
TITLE = ''
VERSION = '0.0.0'
AUTHOR = 'Jamie E Paton'
TEST = 0

import sys
import logging
import unittest
import hypothesis as hs

from jsonobject import JSONObject

class LessonPlan(JSONObject):
        def __init__(self, key_stage, subject, specification_point, national_curriculum_link,
                     previous_lesson_link, topic, title, subtile, sequence_id, learning_objectives,
                     activities, homework, key_terms, resources, group, date, time):
            self.key_stage = key_stage
            self.subject = subject
            self.specification_point = specification_point
            self.national_curriculum_link = national_curriculum_link
            self.previous_lesson_link = previous_lesson_link
            self.topic = topic
            self.title = title
            self.subtitle = subtitle
            
            self.sequence_id = sequence_id
            self.learning_objectives = learning_objectives
            self.activities = activities
            self.homework = homework
            self.key_terms = key_terms
            self.resources = resources
            
            self.group = group
            self.date = date
            self.time = time

def main(args):
    
    return None
    
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


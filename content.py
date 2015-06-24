# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:53:54 2015

@author: Jamie
"""
TITLE = 'lesson content'
VERSION = '0.0.1'
AUTHOR = 'Jamie E Paton'
TEST = 0

import sys
import logging
import unittest
import hypothesis as hs

class LessonContent(jsonobject.JSONObject):
    """
    Holds lesson content related information.
    """
    def __init__(self,
                 key_stage,
                 subject,
                 specification_point,
                 national_curriculum_link,
                 previous_lesson_link,
                 topic,
                 title,
                 subtitle,
                 sequence_id):
        super(type(self), self).__init__()
        self.key_stage = key_stage
        self.subject = subject
        self.specification_point = specification_point
        self.national_curriculum_link = national_curriculum_link
        self.previous_lesson_link = previous_lesson_link
        self.topic = topic
        self.title = title
        self.subtitle = subtitle
        self.sequence_id = sequence_id

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


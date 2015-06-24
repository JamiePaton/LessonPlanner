# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:54:04 2015

@author: Jamie
"""
TITLE = 'lessonplan logistics'
VERSION = '0.0.1'
AUTHOR = 'Jamie E Paton'
TEST = 0

import sys
import logging
import unittest
import hypothesis as hs

class LessonLogistics(jsonobject.JSONObject):
    """
    Holds information about the date, time and group for this lesson.
    """
    def __init__(self,
                 group,
                 date,
                 time):
        super(type(self), self).__init__()
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


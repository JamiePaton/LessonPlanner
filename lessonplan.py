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

class LessonPlan(object):
    """
    Attributes
    ----------
    
    Methods
    -------
    
    Notes
    -----
    
    """
    def __init__(self):
        pass

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


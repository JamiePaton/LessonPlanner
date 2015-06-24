# -*- coding: utf-8 -*-
"""
Implements main logic for the Lesson Planner application

Created on Sat Jun 20 23:29:56 2015

@author: Jamie E Paton
"""
TITLE = 'Lesson Planner'
VERSION = '0.0.3'
AUTHOR = 'Jamie E Paton'
TEST = 0

import sys
import os
import time
import datetime as dt

import logging
import logging.config

import hypothesis as hs
import unittest

import json
import jsonobject

import content, teaching, logistics

class LessonPlan(jsonobject.JSONObject):
    """
    Holds information for a lesson plan.
    
    Attributes
    ----------
    content : LessonContent
        Holds lesson content related information.
    teaching : LessonTeaching
        Holds information about the teaching / delivery of content. 
    logistics : LessonLogistics, optional
        Holds information about the date, time and group for this lesson.
    """
    def __init__(self, content, teaching, logistics=None):
        logger.info('Initialising lesson.')
        super(type(self), self).__init__()
        
        logger.debug("content:\n{}".format(str(content)))
        self.content = content
        
        logger.debug("teaching:\n{}".format(str(teaching)))
        self.teaching = teaching
        
        logger.debug("logistics:\n{}".format(str(logistics)))
        self.logistics = logistics


def save_lesson(lesson, filename=None):
    if filename is None:
        filename = "{0} {1} L{2}.json".format(lesson.content.specification_point,
                             lesson.content.title,
                             lesson.content.sequence_id)
    with open(filename, 'w') as jsonfile:
        jsonfile.write(str(lesson))


def imports():
    import types
    for name, val in globals().items():
        if isinstance(val, types.ModuleType):
            yield val.__name__

def load_lesson(filename):
    logger.debug('#     loading lesson from {}'.format(filename))
    lesson_dict = jsonobject.load_json_file(filename)
    logger.debug(str(lesson_dict))
    print globals()[lesson_dict['_type'].split('.')[1]]('content', 'teaching', 'logistics')

def setup_logging(default_path='logs/loggingconfig.json', default_level=logging.INFO,
                  env_key='LOG_CFG'):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

# TODO Category class

def main(args):
    teaching.CommandWord('hello', 'greeting').save_to_file('cw.json')
    print type(jsonobject.JSONObject.load_from_file('cw.json')).__name__





if __name__ == '__main__':
    setup_logging(default_level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.info(''.join([TITLE, ' v', VERSION, ' ', AUTHOR]))
    logger.debug('Imported modules:\n\n\t' + '\n\t'.join(list(imports())))
    sys.exit(main(sys.argv))

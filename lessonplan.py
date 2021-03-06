# -*- coding: utf-8 -*-
"""
Implements main logic for the Lesson Planner application

Created on Sat Jun 20 23:29:56 2015

@author: Jamie E Paton
"""
TITLE = 'Lesson Planner'
VERSION = '0.0.4'
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

class LessonTeaching(jsonobject.JSONObject):
    """
    Holds information about the teaching / delivery of content. 
    
    Attributes
    ----------
    learning_objectives : list
        a list of learning objectives for the lesson
    activities : list
        a list of activities for the lesson
    """
    def __init__(self,
                 learning_objectives,
                 activities):
        super(type(self), self).__init__()
        self.learning_objectives = learning_objectives
        self.activities = activities

class LearningObjective(jsonobject.JSONObject):
    def __init__(self,
                 command,
                 skill_statement,
                 success_criteria=None,
                 context=None,
                 level=None):
        super(type(self), self).__init__()
        self.command = command
        self.skill_statement = skill_statement
        self.context = context
        if success_criteria is None and context is not None:
            self.success_criteria = ' '.join(['I can', self.command.word,
                                              self.skill_statement, self.context])
        if level is None:
            self.level = self.command.level



class CommandWord(jsonobject.JSONObject):
    def __init__(self, word, level, description=None):
        super(type(self), self).__init__()
        self.word = word
        self.level = level
        self.description = description


class Activity(jsonobject.JSONObject):
    def __init__(self,
                 title,
                 category,
                 teacher_activity,
                 pupil_activity,
                 pupil_learning,
                 assessment_for_learning,
                 differentiation,
                 directions,
                 notes,
                 length,
                 risk_assessment,
                 resources,
                 order=None):
        super(type(self), self).__init__()
        self.title = title
        self.category = category
        self.teacher_activity = teacher_activity
        self.pupil_activity = pupil_activity
        self.pupil_learning = pupil_learning
        self.assessment_for_learning = assessment_for_learning
        self.differentiation = differentiation
        self.directions = directions
        self.notes = notes
        self.length = length
        self.risk_assessment = risk_assessment
        self.resources = resources
        self.order = order


class Resource(jsonobject.JSONObject):
    def __init__(self, name, responsible_person=None, risk_assessment=None, quantitiy=None, 
                 notes=None):
        super(type(self), self).__init__()
        self.name = name
        self.responsible_person = responsible_person
        self.risk_asssessment = risk_assessment
        self.quantity = quantity
        self.notes = notes


class RiskAssessment(jsonobject.JSONObject):
    def __init__(self, risk, severity, chance, control_measures):
        super(type(self), self).__init__()
        self.risk = risk
        self.severity = severity
        self.chance = chance
        self.control_measures = control_measures

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
    CommandWord('hello', 'greeting').save_to_file('cw.json')
    print type(jsonobject.JSONObject.load_from_file('cw.json')).__name__





if __name__ == '__main__':
    setup_logging(default_level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.info(''.join([TITLE, ' v', VERSION, ' ', AUTHOR]))
    logger.debug('Imported modules:\n\n\t' + '\n\t'.join(list(imports())))
    sys.exit(main(sys.argv))

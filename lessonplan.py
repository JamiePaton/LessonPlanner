# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 23:29:56 2015

@author: Jamie
"""
TITLE = 'Lesson Planner'
VERSION = '0.0.2'
AUTHOR = 'Jamie E Paton'
TEST = 0

import sys
import logging
import unittest
import hypothesis as hs
import datetime as dt
import time
import pprint

import jsonobject

class LessonPlan(jsonobject.JSONObject):
    def __init__(self, content, teaching, logistics):
        self.content = content
        self.teaching = teaching
        self.logistics = logistics

class LessonContent(jsonobject.JSONObject):
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
    def __init__(self,
                 learning_objectives,
                 activities):
        self.learning_objectives = learning_objectives
        self.activities = activities

class LessonLogistics(jsonobject.JSONObject):
    def __init__(self,
                 group,
                 date,
                 time):
        self.group = group
        self.date = date
        self.time = time

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
                 order):
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

class RiskAssessment(jsonobject.JSONObject):
    def __init__(self, risk, severity, chance, control_measures):
        self.risk = risk
        self.severity = severity
        self.chance = chance
        self.control_measures = control_measures

class CommandWord(jsonobject.JSONObject):
    def __init__(self, word, level):
        self.word = word
        self.level = level

class LearningObjective(jsonobject.JSONObject):
    def __init__(self, 
                 command,
                 skill_statement,
                 success_criteria=None,
                 context=None,
                 level=None):

        self.command = command
        self.skill_statement = skill_statement
        self.context = context
        if success_criteria is None and context is not None:
            self.success_criteria = ' '.join(['I can', self.command.word, 
                                              self.skill_statement, self.context])
        if level is None:
            self.level = self.command.level

def save_lesson(lesson, filename=None):
    if filename is None:
        filename = "{} {} L{}.json".format(lesson.content.specification_point,
                             lesson.content.title,
                             lesson.content.sequence_id)
        with open(filename, 'w') as jsonfile:
            jsonfile.write(str(lesson))

def load_lesson(filename):
    logger.debug('#     loading lesson from {}'.format(filename))
    lesson_dict = jsonobject.load_json_file(filename)
    logger.debug(str(lesson_dict))
    
    content = LessonContent(**lesson_dict['content'])
    logger.debug(str(content))
    
    logger.debug('#     create and populate learning objective list')
    learning_objectives = []
    for lo in lesson_dict['teaching']['learning_objectives']:
        logger.debug(str(lo))
        lo['command'] = CommandWord(**lo['command'])
        learning_objectives.append(lo)
    
    logger.debug('#     create and populate activities list')
    activities = []
    for act in lesson_dict['teaching']['activities']:
        logger.debug(str(act))
        activities.append(act)
        
    teaching = LessonTeaching(learning_objectives, activities)
    
    logistics = LessonLogistics(**lesson_dict['logistics'])
    logger.debug(str(logistics)) 
    
    return LessonPlan(content, teaching, logistics)

def main(args):
#    # Define learning objectives
#    cw1 = CommandWord('describe', 'knowledge')    
#    cw2 = CommandWord('explain', 'understanding')    
#    cw3 = CommandWord('suggest', 'evaluation')
#    
#    lo1 = LearningObjective(cw1, 'the structure', context='of the national grid')
#    lo2 = LearningObjective(cw2, 'the dangers', context='of mains electricity')
#    lo3 = LearningObjective(cw3, 'safety measures', context='to protect from electrocution')
#    
#    content = LessonContent(4, 'physics', 'P2.4.2', 'physics at home', 'DC electricity', 'AC electricity', 'The National Grid', 'How do we get electricity?', 1)
#    act1 = Activity(title = 'exam question',
#             category = 'exam technique',
#             teacher_activity = None,
#             pupil_activity = 'attempt to answer exam question from a previous paper',
#             pupil_learning = 'consolidation of previous learning',
#             assessment_for_learning = None,
#             differentiation = None,
#             directions = None,
#             notes = None,
#             length = '10 minutes',
#             risk_assessment = None,
#             resources = None,
#             order = 3)
#    teaching = LessonTeaching([lo1, lo2, lo3], [act1])
#    logistics = LessonLogistics('7K5', time.mktime(dt.datetime.today().timetuple()), '10')
#    lesson = LessonPlan(content, teaching, logistics)
#    save_lesson(lesson)
    lesson = load_lesson('P2.4.2 The National Grid L1.json')
    #print lesson
    
    
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
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.info(''.join([TITLE, ' v', VERSION, ' ', AUTHOR]))
    sys.exit(main(sys.argv))


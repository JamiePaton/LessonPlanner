# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 23:29:56 2015

@author: Jamie
"""
TITLE = 'Lesson Planner'
VERSION = '0.0.1'
AUTHOR = 'Jamie E Paton'
TEST = 0

import sys
import logging
import unittest
import hypothesis as hs

import jsonobject

class LessonPlan(jsonobject.JSONObject):
    def __init__(self, content, delivery, logistics):
        self.content = content
        self.delivery = delivery
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
                 subtitle):
        self.key_stage = key_stage
        self.subject = subject
        self.specification_point = specification_point
        self.national_curriculum_link = national_curriculum_link
        self.previous_lesson_link = previous_lesson_link
        self.topic = topic
        self.title = title
        self.subtitle = subtitle


class LessonTeaching(jsonobject.JSONObject):
    def __init__(self,
                 learning_objectives):
        self.learning_objectives = learning_objectives

class LessonLogistics(jsonobject.JSONObject):
    pass

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
                 resources):
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

def main(args):
    # Define learning objectives
    cw1 = CommandWord('describe', 'knowledge')    
    cw2 = CommandWord('explain', 'understanding')    
    cw3 = CommandWord('suggest', 'evaluation')
    
    lo1 = LearningObjective(cw1, 'the structure', context='of the national grid')
    lo2 = LearningObjective(cw2, 'the dangers', context='of mains electricity')
    lo3 = LearningObjective(cw3, 'safety measures', context='to protect from electrocution')
    
    content = LessonContent(4, 'physics', 'P2.4.2', 'physics at home', 'DC electricity', 'AC electricity', 'The National Grid', 'How do we get electricity?')
    teaching = LessonTeaching([lo1, lo2, lo3])
    logistics = LessonLogistics()
    lesson = LessonPlan(content, teaching, logistics)
    print lesson
    
    
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


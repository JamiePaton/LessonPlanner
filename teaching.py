# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:53:59 2015

@author: Jamie
"""
TITLE = 'lessonplan teaching'
VERSION = '0.0.1'
AUTHOR = 'Jamie E Paton'
TEST = 0

import sys
import logging
import unittest
import hypothesis as hs
import jsonobject

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
    def __init__(self, word, level):
        super(type(self), self).__init__()
        self.word = word
        self.level = level


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


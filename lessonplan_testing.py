# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:52:25 2015

@author: Jamie
"""
TITLE = 'lessonplan testing'
VERSION = '0.0.1'
AUTHOR = 'Jamie E Paton'
TEST = 0

import sys
import logging
import unittest
import hypothesis as hs



def main(args):
    # Define learning objectives
    cw1 = CommandWord('describe', 'knowledge')
    cw2 = CommandWord('explain', 'understanding')
    cw3 = CommandWord('suggest', 'evaluation')

    lo1 = LearningObjective(cw1, 'the structure', context='of the national grid')
    lo2 = LearningObjective(cw2, 'the dangers', context='of mains electricity')
    lo3 = LearningObjective(cw3, 'safety measures', context='to protect from electrocution')
    
    content = LessonContent(4, 'physics', 'P2.4.2', 'physics at home', 'DC electricity', 'AC electricity', 'The National Grid', 'How do we get electricity?', 1)
    act1 = Activity(title = 'exam question',
             category = 'exam technique',
             teacher_activity = None,
             pupil_activity = 'attempt to answer exam question from a previous paper',
             pupil_learning = 'consolidation of previous learning',
             assessment_for_learning = None,
             differentiation = None,
             directions = None,
             notes = None,
             length = '10 minutes',
             risk_assessment = None,
             resources = None,
             order = 3)
    teaching = LessonTeaching([lo1, lo2, lo3], [act1])
    logistics = LessonLogistics('7K5', time.mktime(dt.datetime.today().timetuple()), '10')
    lesson = LessonPlan(content, teaching, logistics)
    print lesson
#    lnn = js.encode(lesson)
#    js.encode()
#    json.dumps()
#    print type(js.decode(lnn)
#    save_lesson(lnn, 'testing2.json')

#    lesson = load_lesson('P2.4.2 The National Grid L1.json')
#    lesson = load_lesson2('testing.json')
    #print lesson
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


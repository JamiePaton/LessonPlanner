# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 18:25:09 2015

@author: Jamie
"""
TITLE = 'GUI Interaction'
VERSION = '0.0.1'
AUTHOR = 'Jamie E Paton'
TEST = 0

import sys
import logging
import unittest
import hypothesis as hs
from atom.api import Atom, Unicode

import lessonplan

class CommandWord_Enaml(Atom):
    word = Unicode()
    level = Unicode()
    description = Unicode()
    
    def save(self):
        CommandWord(self.word, self.level,                  self.description).save_to_file('templates/commandwords/{0}.json'.format(self.word))

def main(args):
    import enaml
    from enaml.qt.qt_application import QtApplication
    with enaml.imports():
        from enaml_views import CommandWordView
    cw = CommandWord_Enaml(word='', level='', description='')
    app = QtApplication()
    view = CommandWordView(commandword=cw)
    view.show()
    app.start()
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

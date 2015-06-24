# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 02:57:12 2014

@author: Jamie
"""
TITLE = 'jsonobject'
VERSION = '0.0.3'
AUTHOR = 'Jamie Paton'
import jsonpickle
import logging

jsonpickle.set_encoder_options('simplejson', sort_keys=True, indent=4)


class JSONObject(object):
    """

    Notes
    -----
    subclasses should call

        super(type(self), self).__init__()
    to get a _type attribute in the JSON file.
    """
    def __init__(self):
        pass

    def save_to_file(self, filename):
        logger = logging.getLogger(__name__)
        logger.info('#     saving json file {1}'.format(filename))
        logger.debug('{1}'.format(str(self)))
        json_string = jsonpickle.encode(self)
        with open(filename, 'w') as jsonfile:
            jsonfile.write(json_string)

    @staticmethod
    def load_from_file(filename):
        logger = logging.getLogger(__name__)
        logger.info('#     loading json file {1}'.format(filename))
        with open(filename, 'r') as jsonfile:
            json_string = jsonfile.read()
        logger.debug('{1}'.format(json_string))
        return jsonpickle.decode(json_string)

    def __repr__(self):
        return jsonpickle.encode(self)


if __name__ == '__main__':
    print ''.join([TITLE, ' v', VERSION, ' ', AUTHOR])

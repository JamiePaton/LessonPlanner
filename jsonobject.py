# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 02:57:12 2014

@author: Jamie
"""
TITLE = ''
VERSION = '0.0.2'
AUTHOR = 'Jamie Paton'
import json
import jsonpickle
import datetime as dt
import time
import logging

jsonpickle.set_encoder_options('simplejson', sort_keys=True, indent=4)

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, dt.datetime):
            print 'fish'
            return int(time.mktime(obj.timetuple()))
        return json.JSONEncoder.default(self, obj)

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
        #self._type = str(self.__class__.__module__ + "." + self.__class__.__name__)
    
    def save_to_file(self, filename):
        json_string = jsonpickle.encode(self)
        with open(filename, 'w') as jsonfile:
            jsonfile.write(json_string)
    
    @staticmethod
    def load_from_file(filename):
        with open(filename, 'r') as jsonfile:
            json_string = jsonfile.read()
        return jsonpickle.decode(json_string)
        
    def __repr__(self):
        return jsonpickle.encode(self)
#        return json.dumps(self, default=lambda o: o.__dict__, 
#                          sort_keys=True, indent=4, cls=Encoder)

def load_json_file(filename):
    logger = logging.getLogger(__name__)
    logger.debug('#     loading json file {}'.format(filename))
    with open(filename, 'r') as jsonfile:
        json_data = json.loads(jsonfile.read())
    return json_data

def save_json_file(filename, json_data):
    with open(filename, 'w') as jsonfile:
        jsonfile.write(json_data)

if __name__ == '__main__':
    print ''.join([TITLE, ' v', VERSION, ' ', AUTHOR])


# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 02:57:12 2014

@author: Jamie
"""
TITLE = ''
VERSION = '0.0.1'
AUTHOR = 'Jamie Paton'
import json

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))
        return json.JSONEncoder.default(self, obj)

class JSONObject(object):
    def __repr__(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
                          sort_keys=True, indent=4, cls=Encoder)

def load_json_file(filename):
    with open(filename, 'r') as jsonfile:
        json_data = jsonfile.read()
    return json_data

def save_json_file(filename, json_data):
    with open(filename, 'w') as jsonfile:
        jsonfile.write(json_data)

if __name__ == '__main__':
    print ''.join([TITLE, ' v', VERSION, ' ', AUTHOR])


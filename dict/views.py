from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect

from django.utils import simplejson

import collections

import string

import os

from satlife.settings import PROJECT_ROOT

# Create your views here.

def word(request, word):
    _file = open(os.path.join(PROJECT_ROOT, '../static/data.json'))
    dict_data = simplejson.loads(string.join(_file.readlines()))
    respond = {}
    result = {}
    rootList = []
    finaldata = dict_data['Entries']
    for entry in finaldata:
        flag = False
        temp =""
        for item in entry['Root']:
            if entry['Type'] == 'prefix':
                if word.startswith(item):
                    result['prefix'] = entry
                    result['prefix_by'] = item
            elif entry['Type'] == 'suffix':
                if word.endswith(item):
                    result['suffix'] = entry
                    result['suffix_by'] = item
            else:
                if word.find(item) != -1:
                    temp = item
                    flag = True
        if flag:
            tmp = {}
            tmp['by'] = temp
            tmp['entry'] = entry
            rootList.append(tmp)
    result['root'] = rootList
    if len(result) == 1 and not result['root']:
        result['empty'] = True
    else:
        result['empty'] = False
    result['request'] = word
    json = simplejson.dumps(result, indent = 2)
    return HttpResponse(json, mimetype='application/json')


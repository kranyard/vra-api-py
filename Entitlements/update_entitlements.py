#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json
import pprint
import requests

import rw

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

pp = pprint.PrettyPrinter(indent=4)

debug = False

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/entitlements/e47e0416-acc0-4669-b73d-88ea98456efe".format(host)

request = rw.getUrl(url,headers)

print json.dumps(request)

newuser = {}

newuser['ref'] = 'joe@corp.local'
newuser['type'] = 'USER'
newuser['value'] = 'Scott 1234'
newuser['tenantName'] = 'vsphere.local'

request['principals'].append(newuser)
request['version'] += 1

print json.dumps(request)

request = rw.putUrl( url, data=json.dumps(request), headers=headers)

print request.text



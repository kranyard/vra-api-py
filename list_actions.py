#!/usr/bin/env python
import operator
import os
import sys
import json
import time
import urllib

import json

import rw

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

machine = urllib.quote(sys.argv[1])

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/consumer/resources?$filter=name%20eq%20'{1}'".format(host,machine)
request = rw.getUrl(url,headers)

c = request["content"][0]
this_id = c ['id']

parent = c['parentResourceRef']
parent_id = parent['id']

tenantLabel=c['organization']['tenantLabel']
tenantRef=c['organization']['tenantRef']
subtenantLabel=c['organization']['subtenantLabel']
subtenantRef=c['organization']['subtenantRef']

url = "https://{0}/catalog-service/api/consumer/resources/{1}/actions".format(host,parent_id)
request = rw.getUrl(url,headers)

print parent['label']
for c in request['content']:
	print "  ",c['name']

url = "https://{0}/catalog-service/api/consumer/resources/{1}/actions".format(host,this_id)
request = rw.getUrl(url,headers)

print machine
for c in request['content']:
	print "  ",c['name']

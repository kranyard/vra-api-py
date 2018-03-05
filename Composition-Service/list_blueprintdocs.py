#!/usr/bin/env python
import operator
import os
import sys
import json

sys.path.append("../")
import rw

debug = False


host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/composition-service/api/blueprintdocuments".format(host)

request = rw.getUrl(url,headers)

if ( debug ):
	print json.dumps(request)
	exit (0)

for item in request['content']:
	print item['name'], item['id']

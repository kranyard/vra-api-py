#!/usr/bin/env python
import operator
import os
import sys
import json

sys.path.append("../")
import rw

debug = False

#docid = sys.argv[1]

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/composition-service/api/blueprints ".format(host)

request = rw.getUrl(url,headers)

if ( debug ):
	print json.dumps(request)
	exit (0)

for item in request['content']:
	for key, value in item.items():
		print key, ':=', value
	print '-----'

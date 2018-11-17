#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json
import pprint

sys.path.append("../")
import rw

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']
tenant = os.environ['VRATENANT']

pp = pprint.PrettyPrinter(indent=4)

debug = True

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/advanced-designer-service/api/resourceOperations?limit=500".format(host, tenant)
request = rw.getUrl(url,headers)

print request["metadata"]

if ( debug ):
	pp.pprint(request)
	print json.dumps(request)
	exit (0)

for item in request['content']:
	print item["name"]

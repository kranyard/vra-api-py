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

url = "https://{0}/properties-service/api/propertygroups".format(host)

request = rw.getUrl(url,headers)

if ( debug ):
	print json.dumps(request)
	exit (0)

for c in request["content"]:
	#print c["label"], c["id"]
	for k, v in c.items():
		if ( k == "id" ):
			print k, v

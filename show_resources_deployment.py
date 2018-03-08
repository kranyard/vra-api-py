#!/usr/bin/env python
import operator
import os
import sys
import json

import rw

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/consumer/resources?limit=99999&$filter=resourceType/name+eq+'Deployment'".format(host)
request = rw.getUrl(url,headers)

#print json.dumps(request)

for x in request["content"]:
	print "RESOURCE ID",x['id'],x['name'], x['catalogItem']['label']
	#for key, value in x.items():
	#	print key, ':=', value
	#print '-----'


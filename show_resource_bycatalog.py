#!/usr/bin/env python
import operator
import os
import sys
import json

import rw

catid = sys.argv[1]

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/consumer/resources?limit=5000&$filter=catalogItem/name+eq+'{1}'+and+resourceType/id+eq+'composition.resource.type.deployment'".format(host,catid)
request = rw.getUrl(url,headers, showUrl=False)

#print json.dumps(request)
#exit(1)

for x in request["content"]:
	print x['id'],x['name'], x['catalogItem']['label']

	parentId = x['id']

	url = "https://{0}/catalog-service/api/consumer/resources/?$filter=parentResource/id+eq+'{1}'+and+resourceType/id+eq+'Infrastructure.Virtual'&limit=5000".format(host,parentId)
	request = rw.getUrl(url,headers)
	#print json.dumps(request)
	
	for y in request['content']:
		print y['name']


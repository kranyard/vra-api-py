#!/usr/bin/env python
import operator
import os
import sys
import json

import rw

machineName = sys.argv[1] 

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/consumer/resources?limit=99999&$filter=name+eq+'{1}'+and+resourceType/id+eq+'Infrastructure.Virtual'".format(host, machineName)
request = rw.getUrl(url,headers)

#print json.dumps(request)

for x in request["content"]:
	print "RESOURCE ID",x['id'],x['name']," Parent Ref ",x['parentResourceRef']['id']
	#for key, value in x.items():
	#	print key, ':=', value
	#print '-----'


	parentResource = x['parentResourceRef']['id']

	url = "https://{0}/catalog-service/api/consumer/resources/{1}".format(host, parentResource)
	request = rw.getUrl(url,headers)
	
	#print json.dumps(request)

	print request['catalogItem']['id']
	print request['catalogItem']['label']


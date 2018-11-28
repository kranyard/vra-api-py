#!/usr/bin/env python
import operator
import os
import sys
import json

import rw

username = sys.argv[1]

showUrl = True

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/consumer/resources?$filter=owners/ref+eq+'{1}'+and+resourceType/name+eq+'Deployment'&limit=500".format(host, username)
request = rw.getUrl(url,headers,showUrl=showUrl)

#print json.dumps(request)
#exit(1)

print request["metadata"]

for x in request["content"]:

	parentId = x['id']
	if ( x["resourceTypeRef"]["label"] != "Virtual Machine" ):
		print "Deployment : "+x["name"]

	url = "https://{0}/catalog-service/api/consumer/resources/?$filter=parentResource/id+eq+'{1}'+and+resourceType/id+eq+'Infrastructure.Virtual'&limit=5000".format(host,parentId)
	request = rw.getUrl(url,headers,showUrl=showUrl)
	
	for y in request['content']:
		resourceId = y["id"]
		url = "https://{0}/catalog-service/api/consumer/resourceViews/{1}".format(host, resourceId)
		rv = rw.getUrl(url,headers,showUrl=showUrl )

		#print y["name"],y["requestId"], y["resourceTypeRef"]["label"]," Power State: ", rv["status"]

		requestId = y["requestId"]
		url = "https://{0}/catalog-service/api/consumer/requests/{1}/resourceViews/?$filter=name+eq+'{2}'".format(host, requestId, y["name"])
		r = rw.getUrl(url,headers,showUrl=showUrl)
		for c in r["content"]: 
			if ( c["resourceType"] == "Infrastructure.Virtual" ):
				if 'data' in c:
					if 'ip_address' in c["data"]:
						print y["name"]+" ["+rv["status"]+"] [" + c["data"]["ip_address"]+"]"
					else:
						print y["name"]+" ["+rv["status"]+"]"


		#rw.showProperties(x)
		#print x['providerBinding']['bindingId']


	print 


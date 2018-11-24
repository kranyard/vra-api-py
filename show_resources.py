#!/usr/bin/env python
import operator
import os
import sys
import json

import rw

username = sys.argv[1]

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/consumer/resources?$filter=owners/ref+eq+'{1}'&limit=500".format(host, username)
request = rw.getUrl(url,headers,showUrl=False)

#print json.dumps(request)
#exit(1)

print request["metadata"]

for x in request["content"]:

	#rw.showProperties(x)
	#print x['providerBinding']['bindingId']

	if ( x["resourceTypeRef"]["label"] == "Virtual Machine" ):

		resourceId = x["id"]
		url = "https://{0}/catalog-service/api/consumer/resourceViews/{1}".format(host, resourceId)
		r = rw.getUrl(url,headers,showUrl=False )

		print x["name"],x["requestId"], x["resourceTypeRef"]["label"]," Power State: ", r["status"]

		#requestId = x["requestId"]
		#url = "https://{0}/catalog-service/api/consumer/requests/{1}/resourceViews".format(host, requestId)
		#for c in r["content"]: 
		#	print "Name: "+c["name"]
		#	if 'data' in c:
		#		if 'ip_address' in c["data"]:
		#			print "   ",c["data"]["ip_address"]

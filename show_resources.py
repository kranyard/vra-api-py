#!/usr/bin/env python
import operator
import os
import sys
import json

import rw

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/consumer/resources".format(host)
request = rw.getUrl(url,headers)

#print json.dumps(request)

for x in request["content"]:

	rw.showProperties(x)
	#print x['providerBinding']['bindingId']

	#if ( x["resourceTypeRef"]["label"] == "Virtual Machine" ):
		#print x["name"],x["requestId"], x["resourceTypeRef"]["label"]
		#requestId = x["requestId"]
		#url = "https://{0}/catalog-service/api/consumer/requests/{1}/resourceViews".format(host, requestId)
		#r = rw.getUrl(url,headers )
		#rw.findProperties(r, "resourceId")

		#for c in r["content"]: 
		#	print "Name: "+c["name"]
		#	if 'data' in c:
		#		if 'ip_address' in c["data"]:
		#			print "   ",c["data"]["ip_address"]

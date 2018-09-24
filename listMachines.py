#!/usr/bin/env python
import operator
import os
import sys
import json

import rw

#name = sys.argv[1]

pageSize=1000

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/consumer/resources?limit={1}".format(host,pageSize)
#url = "https://{0}/catalog-service/api/consumer/resources?$filter=name eq '{1}'".format(host, name)


flag=True
while flag:

	request = rw.getUrl(url,headers)
	print json.dumps(request["metadata"])

	url=False
	for l in request["links"]:
		if l["rel"] == "next":
			url = l["href"]

	if (not url):
		flag = False

	for x in request["content"]:
		#rw.showProperties(x)
		if ( x["resourceTypeRef"]["label"] == "Virtual Machine" ):
			print x['name'], x['providerBinding']['bindingId'] ,x["requestId"], x["resourceTypeRef"]["label"]
			requestId = x["requestId"]

			#url = "https://{0}/catalog-service/api/consumer/requests/{1}/resourceViews".format(host, requestId)
			#r = rw.getUrl(url,headers )
			#rw.showProperties(r["content"][0])
			#print "Endpoint Ext ref", r["content"][0]["data"]["endpointExternalReferenceId"]

			#for c in r["content"]: 
			#	print "Name: "+c["name"]
			#	if 'data' in c:
			#		if 'ip_address' in c["data"]:
			#			print "   ",c["data"]["ip_address"]

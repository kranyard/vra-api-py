#!/usr/bin/env python
import operator
import os
import sys
import json

import rw

username = sys.argv[1]
machinename = sys.argv[2]

showUrl = False

simple = False

pageSize=1000

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

#url = "https://{0}/catalog-service/api/consumer/resources?$filter=owners/ref+eq+'{1}'&limit={2}".format(host, username, pageSize)
#url = "https://{0}/catalog-service/api/consumer/resources?limit={1}".format(host, pageSize)
url = "https://{0}/catalog-service/api/consumer/resources?$filter=owners/ref+eq+'{1}'+and+substringof('{2}', name)&limit={3}".format(host, username, machinename, pageSize )

flag=True
while flag:

	request = rw.getUrl(url,headers, showUrl=showUrl)

	#print request["metadata"]

	url=False
	for l in request["links"]:
		if l["rel"] == "next":
			url = l["href"]

	if (not url):
		flag = False

	for x in request["content"]:
		if ( x["resourceTypeRef"]["label"] == "Virtual Machine" ):

			if ( simple ):
				print x["name"]
			else:
				resourceId = x["id"]
				#print "Resource ID : "+resourceId ;

				url = "https://{0}/catalog-service/api/consumer/resourceViews/{1}".format(host, resourceId)
				request = rw.getUrl(url,headers, showUrl=showUrl)

				print request["name"],request["status"]

				#print x['name'], x['providerBinding']['bindingId'] ,x["requestId"], x["resourceTypeRef"]["label"]
				#requestId = x["requestId"]

				#url = "https://{0}/catalog-service/api/consumer/requests/{1}/resourceViews".format(host, requestId)
				#r = rw.getUrl(url,headers , showUrl=showUrl)
				#print "Endpoint Ext ref", r["content"][0]["data"]["endpointExternalReferenceId"]

				for c in r["content"]: 
					print "Name: "+c["name"]
					if 'data' in c:
						if 'ip_address' in c["data"]:
							print "   ",c["data"]["ip_address"]




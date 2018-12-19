#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json
import pprint

import rw

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

providerBindingId = sys.argv[1]

pp = pprint.PrettyPrinter(indent=4)

debug = False

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

#url = "https://{0}/catalog-service/api/consumer/resourceViews?$filter=providerBinding/bindingId eq '{1}'".format(host, providerBindingId)
url = "https://{0}/catalog-service/api/consumer/resources?$filter=name eq '{1}'&withExtendedData=true&withOperations=true".format(host, providerBindingId)
#url = "https://{0}/catalog-service/api/consumer/resources?$filter=name eq '{1}'".format(host, providerBindingId)

url = "https://{0}/catalog-service/api/consumer/resourceViews?$filter=name eq '{1}'&withExtendedData=true&withOperations=true".format(host, providerBindingId)

request = rw.getUrl(url,headers, showUrl=False)

#print request["metadata"]
print json.dumps(request)
exit(1)

resourceId = request["content"][0]["resourceId"]
print "Resource ID: "+resourceId

response = ""
action = ""

if 'links' not in request["content"][0]:
	print request
	print machine+" :: No links in response"
	exit(1)

for c in request["content"][0]['links']:
	print c['rel']
	if ("PowerOff" in c['rel']):
		if ("GET" in c['rel']):
			gUrl=c['href']
		if ("POST" in c['rel']):
			pUrl=c['href']
			action = "Power Off"

	if ("PowerOn" in c['rel']):
		if ("GET" in c['rel']):
			gUrl=c['href']
		if ("POST" in c['rel']):
			pUrl=c['href']
			action = "Power On"

print "resource ID : "+resourceId+" : "+action

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
url = "https://{0}/catalog-service/api/consumer/resourceViews?$filter=name eq '{1}'".format(host, providerBindingId)

request = rw.getUrl(url,headers)

resourceId = request["content"][0]["resourceId"]
print "Resource ID : "+resourceId ;

requestId = request["content"][0]["requestId"]
print "Request ID : "+requestId ;

#url = "https://{0}/catalog-service/api/consumer/resources/{1}/actions".format(host, resourceId)
#request = rw.getUrl(url,headers)

url="https://{0}/catalog-service/api/consumer/requests/{1}/resourceViews".format(host,requestId)
request = rw.getUrl(url,headers)

for c in request["content"]:
	print c["name"], c["status"]

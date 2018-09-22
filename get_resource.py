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

#print request["metadata"]
print json.dumps(request)

print "Resource ID: "+request["content"][0]["resourceId"]

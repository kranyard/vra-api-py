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

print request["metadata"]

#print json.dumps(request)

for x in request["content"]:
	print x["name"],x["requestId"], x["resourceTypeRef"]["label"]


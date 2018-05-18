#!/usr/bin/env python
import operator
import os
import sys
import json

sys.path.append("../")
import rw

group = sys.argv[1]

debug = False

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/properties-service/api/propertygroups/{1}".format(host, group)

request = rw.getUrl(url,headers)

if ( debug ):
	print json.dumps(request)
	exit (0)

#print request["label"], request["id"]

for k,v in request["properties"].items():
	print k, v["facets"]["defaultValue"]["value"]["value"]

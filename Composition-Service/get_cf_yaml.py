#!/usr/bin/env python
import operator
import os
import sys
import json

sys.path.append("../")
import rw

docid = sys.argv[1]

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/composition-service/api/blueprints/{1}/forms/requestform".format(host,docid)

request = rw.getUrl(url,headers, showUrl=False)

form =  json.loads(request)

print request


for p in form["layout"]["pages"]:
	print p["title"]
	for s in p["sections"]:
		for f in s["fields"]:
			print f

print form["layout"]["pages"][0]["sections"][2]["fields"][0]["state"]["read-only"]

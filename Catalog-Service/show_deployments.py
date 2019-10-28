#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json

import rw

pageSize=500

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

debug = False
showUrl = True

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/consumer/deployments?limit={1}".format(host, pageSize)

#print (request["metadata"])

while url:

	request = rw.getUrl(url,headers, showUrl=showUrl)

	if ( debug ):
		print json.dumps(request)
		exit (0)

	url=False
	for l in request["links"]:
		if l["rel"] == "next":
			url = l["href"]

	for item in request['content']:
		print (item['name'],item['id'])

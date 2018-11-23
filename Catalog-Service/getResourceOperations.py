#!/usr/bin/env python
import operator
import os
import sys
import json

import rw

pageSize=1000

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/resourceOperations?limit={1}".format(host,pageSize)

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

	for c in request["content"]:
		print c["name"], c["id"]

#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json

import rw

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

name = sys.argv[1]

pageSize=100

showUrl = False

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

#url = "https://{0}/catalog-service/api/consumer/resourceViews?$filter=substringof('{1}', name)&limit={2}".format(host, name, pageSize)
url = "https://{0}/catalog-service/api/consumer/resourceViews?$filter=substringof('{1}', name)&withExtendedData=true&withOperations=true&limit={2}".format(host, name, pageSize)

while url:

	request = rw.getUrl(url,headers, showUrl=showUrl)

	#print request["metadata"]

	for c in request["content"]:
		print c["name"],c["status"]

	url=False
	for l in request["links"]:
		if l["rel"] == "next":
			url = l["href"]


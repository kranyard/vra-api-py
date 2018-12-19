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
entitledView = False

headers = "-H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"".format(id)
#headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

if entitledView:
	url = "https://{0}/catalog-service/api/consumer/entitledCatalogItemViews?limit={1}".format(host, pageSize)
else:
	url = "https://{0}/catalog-service/api/consumer/catalogItems?limit={1}".format(host, pageSize)


#print request["metadata"]

if ( debug ):
	print json.dumps(request)
	exit (0)

while url:

	request = rw.getUrl(url,headers, showUrl=showUrl)
	print json.dumps(request["metadata"])

	url=False
	for l in request["links"]:
		if l["rel"] == "next":
			url = l["href"]

	for item in request['content']:
		if entitledView:
			print item['name']+" - catalogId: ["+item['catalogItemId']+"] - iconId : ["+item['iconId']+"]"
		else:
			print item['name']+" - catalogId: ["+item['id']+"] - iconId : ["+item['iconId']+"]"

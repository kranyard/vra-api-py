#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json
import pprint

import urllib

sys.path.append("../")
import rw

pageSize=1000

bgName = sys.argv[1]

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']
tenant = os.environ['VRATENANT']

pp = pprint.PrettyPrinter(indent=4)

debug = True

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

# Get subTenantId (Business Group ID) from name
url="https://{0}/identity/api/tenants/{1}/subtenants?$filter=name eq '{2}'".format(host, tenant, bgName)

request = rw.getUrl(url,headers,showUrl=False)

for c in request["content"]:
	#print "Business group ID "+c["id"]
	bgId = c["id"]


#url = "https://{0}/reservation-service/api/reservations?$filter=substringof('QA',name)".format(host)

url = "https://{0}/reservation-service/api/reservations?limit={1}&$filter=subTenantId eq '{2}'".format(host, pageSize, bgId)

flag=True
while flag:

	request = rw.getUrl(url,headers,showUrl=False)

	url=False
	for l in request["links"]:
		if l["rel"] == "next":
			url = l["href"]
	if (not url):
		flag = False

	if ( debug ):
		print json.dumps(request)
		exit (0)

	for item in request['content']:
		for e in item["extensionData"]["entries"]:
			if ("computeResource" in e["key"]):
				computeResource = e["value"]["label"]

			if ("reservationStorages" in e["key"]):
				for i in e["value"]["items"]:
					for v in i["values"]["entries"]:
						if ("storagePath" in v["key"]) :
							storagePath = v["value"]["label"]


		print "["+item["name"]+"]", storagePath, "["+computeResource+"]"

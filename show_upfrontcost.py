#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import rw
import urllib

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']
tenant = os.environ['VRATENANT']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

blueprint = urllib.quote(sys.argv[1])
busgroup = sys.argv[2]

# Get subtenantRef
url="https://{0}/identity/api/tenants/{1}/subtenants".format(host, tenant)
request = rw.getUrl(url,headers)

for c in request["content"]:
	if ( c["name"] == busgroup ):
		print c["name"], c["id"]
		subtenantRef = c["id"]
		
url="https://{0}/composition-service/api/blueprints/?$filter=name%20eq%20'{1}'".format(host, blueprint)
request = rw.getUrl(url,headers)

blueprintId = request["content"][0]["id"]

url="https://{0}/composition-service/api/blueprints/{1}".format(host, blueprintId)
request = rw.getUrl(url,headers)

for c in request["components"]:
	if ( request["components"][c]["type"] == "Infrastructure.CatalogItem.Machine.Virtual.vSphere" ):
		print c
		machineName = c

		getCostJson = {"blueprintId":blueprintId ,"requestedFor":"fritz@vsphere.local","subTenantId": subtenantRef ,"requestData":{"entries":[{"key":"_leaseDays"},{"key":machineName,"value":{"type":"complex","values":{"entries":[]}}}]}}

		url = "https://{0}/composition-service/api/blueprints/{1}/costs/upfront".format(host, blueprintId)
		r=rw.postUrl(url,headers=headers,data=json.dumps(getCostJson))

		c = r.json()

		print json.dumps(c)
		
		for c in r.json():
			fieldMap = c['fieldMap']

			print c["componentId"]

			for i in fieldMap:
				print i, fieldMap[i]['displayString'], fieldMap[i]['min'], fieldMap[i]['max']

			totalLease = c['totalLeasePriceInfo']
			print "totalLease", totalLease['displayString'], totalLease['min'], totalLease['max']

			averageDailyPriceInfo = c['averageDailyPriceInfo']
			print "averageDailyPriceInfo", averageDailyPriceInfo['displayString'], averageDailyPriceInfo['min'], averageDailyPriceInfo['max']

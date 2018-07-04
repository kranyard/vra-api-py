#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import rw

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']
tenant = os.environ['VRATENANT']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

blueprint = sys.argv[1]
busgroup = sys.argv[2]

# Get subtenantRef
url="https://{0}/identity/api/tenants/{1}/subtenants".format(host, tenant)
request = rw.getUrl(url,headers)

for c in request["content"]:
	if ( c["name"] == busgroup ):
		print c["name"], c["id"]
		subtenantRef = c["id"]
		
url="https://{0}/composition-service/api/blueprints/{1}".format(host, blueprint)
request = rw.getUrl(url,headers)

for c in request["components"]:
	if ( request["components"][c]["type"] == "Infrastructure.CatalogItem.Machine.Virtual.vSphere" ):
		print c
		machineName = c

		getCostJson = {"blueprintId":blueprint ,"requestedFor":"fritz@vsphere.local","subTenantId": subtenantRef ,"requestData":{"entries":[{"key":"_leaseDays"},{"key":machineName,"value":{"type":"complex","values":{"entries":[]}}}]}}

		url = "https://{0}/composition-service/api/blueprints/{1}/costs/upfront".format(host, blueprint)
		r=rw.postUrl(url,headers=headers,data=json.dumps(getCostJson))

		#print r.json()
		#rw.showProperties(r.json())

		c = r.json()
		print json.dumps(c[0])

		print c[0]['count']

#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json
import pprint

import rw

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

pp = pprint.PrettyPrinter(indent=4)

debug = False

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}
url = "https://{0}/reservation-service/api/reservations/types".format(host)
url = "https://{0}/reservation-service/api/data-service/schema/Infrastructure.Reservation.Virtual.vSphere/default".format(host)
rsv_schema = rw.getUrl(url,headers)
pp.pprint(rsv_schema)

url = "https://{0}/identity/api/tenants/vsphere.local/subtenants".format(host)
request = rw.getUrl(url,headers)

#print json.dumps(request)

for item in request['content']:
	print "SUBTENANT: ", item['@type'],item['name'], item['id']


url = "https://{0}/reservation-service/api/data-service/schema/Infrastructure.Reservation.Virtual.vSphere/default/computeResource/values".format(host)
data = "{}"
request = rw.postUrl(url,headers,data=data)
print json.dumps(request.json())

item = request.json()
for key, value in item.items():
	if isinstance(value, dict):
		print "--DICT"
		for k, v in value.items():	
			print "  ",k,"::=",v
	elif isinstance(value, list):
		print "--LIST"
		for v in value:	
			print v
	else:
		print key, ':=', value
print '-----'

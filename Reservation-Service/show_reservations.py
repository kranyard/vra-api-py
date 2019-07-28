#!/usr/bin/env python
import operator
import os
import sys
import json
import time
import urllib

import json

sys.path.append("../")
import rw

pageSize=1000

#computeResource = sys.argv[1]
tenantId = sys.argv[1]

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

debug = False

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

#url = "https://{0}/reservation-service/api/reservations?limit={1}".format(host, pageSize)
#url = "https://{0}/reservation-service/api/reservations?$filter=substringof('IPAM',name)".format(host)
#url = "https://{0}/reservation-service/api/reservations?$filter=name eq 'Dev Cluster Reservation'".format(host)

#name = "Dev Cluster Reservation"
#url = "https://{0}/reservation-service/api/reservations/?$filter=name eq '{1}'".format(host, name)
url = "https://{0}/reservation-service/api/reservations/?$filter=tenantId eq '{1}'".format(host, tenantId)


flag=True
while flag:

	request = rw.getUrl(url,headers, showUrl=False)

	url=False
	for l in request["links"]:
		if l["rel"] == "next":
			url = l["href"]
	if (not url):
		flag = False

	if ( debug ):
		print json.dumps(request)
		exit (0)

	print request['metadata']

	for item in request['content']:
		print item["name"], item["id"]
		#for e in item["extensionData"]["entries"]:
		#	if ( ("classId" in e["value"]) and (e["value"]["classId"] == "ComputeResource") ) :
		#		#if ( e["value"]["label"] == computeResource ) :
		#		print item['name'], item['id'], "Compute Resource: "+e["value"]["label"]

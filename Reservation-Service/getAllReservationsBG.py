#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json
import pprint

sys.path.append("../")
import rw

pageSize=1000

bgid = sys.argv[1]

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

pp = pprint.PrettyPrinter(indent=4)

debug = False

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

#url = "https://{0}/reservation-service/api/reservations?$filter=substringof('QA',name)".format(host)

url = "https://{0}/reservation-service/api/reservations?limit={1}&$filter=subTenantId eq '{2}'".format(host, pageSize, bgid)

flag=True
while flag:

	request = rw.getUrl(url,headers)
	
	url=False
	for l in request["links"]:
		if l["rel"] == "next":
			url = l["href"]
	if (not url):
		flag = False

	if ( debug ):
		pp.pprint(request)
		#print json.dumps(request)
		exit (0)

	for item in request['content']:
		for e in item["extensionData"]["entries"]:
			if ( ("classId" in e["value"]) and (e["value"]["classId"] == "ComputeResource") ) :
				#if ( e["value"]["label"] == computeResource ) :
				print item['name'], item['id'], "Compute Resource: "+e["value"]["label"]

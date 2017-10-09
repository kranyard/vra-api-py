#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json
import pprint

import rw

machineName = sys.argv[1]

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/iaas-proxy-provider/api/network/profiles?limit=9999".format(host)
request = rw.getUrl(url,headers)

for netProf in request['content']:
	if (netProf["@type"] == "ExternalNetworkProfile"):

		url = "https://{0}/iaas-proxy-provider/api/network/profiles/addresses/{1}?$filter=virtualMachineName%20eq%20'{2}'".format(host,netProf['id'],machineName)
		req = rw.getUrl(url,headers)

		if (req['metadata']['totalElements'] < 1 ):
			continue
		else:
			print ("Network Profile: "+netProf["name"])
			item = req['content'][0]
			print ("IPv4Address: "+item['IPv4Address'])
			print ("state: "+item['state'])
			print ("virtualMachineName: "+item['virtualMachineName'])
			print ("virtualMachineId: "+item['virtualMachineId'])


			break


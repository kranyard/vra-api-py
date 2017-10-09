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

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/iaas-proxy-provider/api/network/profiles?limit=9999".format(host)
request = rw.getUrl(url,headers)

for item in request['content']:
	if (item["@type"] == "ExternalNetworkProfile"):
		print (item["name"])

		url = "https://{0}/iaas-proxy-provider/api/network/profiles/{1}".format(host,item['id'])
		req = rw.getUrl(url,headers)
		
		definedRanges = req['definedRanges']
		for r in definedRanges:
			print ("Range: ",r["name"])
			for a in r['definedAddresses']:
				if (a['state'] != "UNALLOCATED"):
					print a['hostName'],a['virtualMachineName'],a['IPv4Address'],a['state']


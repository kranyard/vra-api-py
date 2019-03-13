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

print request

for item in request['content']:
	if (item["@type"] == "ExternalNetworkProfile"):
		print (item["@type"]+":: "+item["name"]+" :: "+item["id"])

		url = "https://{0}/iaas-proxy-provider/api/network/profiles/{1}".format(host,item['id'])
		req = rw.getUrl(url,headers)
		
		definedRanges = req['definedRanges']
		for r in definedRanges:
			print ("Range: ",r["name"])
			allocated=0
			expired=0
			unallocated=0
			for a in r['definedAddresses']:
				if (a['state'] == "UNALLOCATED"):
					unallocated+=1
				elif ( a['state'] == "ALLOCATED"):
					allocated+=1
					#print a['hostName'],a['virtualMachineName'],a['IPv4Address'],a['state']
				elif ( a['state'] == "EXPIRED"):
					expired+=1
				else:
					print "Unknown state"
		
			print ("UNALLOCATED : "+str(unallocated)+" ALLOCATED : "+str(allocated)+" EXPIRED : "+str(expired)) 

		url = "https://{0}/iaas-proxy-provider/api/network/profiles/addresses/{1}?limit=9999".format(host,item['id'])
		req = rw.getUrl(url,headers)
		
		allocated=0
		expired=0
		unallocated=0
		for r in req["content"]:
			if (r['state'] == "UNALLOCATED"):
				unallocated+=1
			elif ( r['state'] == "ALLOCATED"):
				allocated+=1
				#print r['hostName'],r['virtualMachineName'],r['IPv4Address'],r['state']
			elif ( r['state'] == "EXPIRED"):
				expired+=1
			else:
				print "Unknown state"
	
		print ("UNALLOCATED : "+str(unallocated)+" ALLOCATED : "+str(allocated)+" EXPIRED : "+str(expired)) 

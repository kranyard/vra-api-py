#!/usr/bin/env python
import operator
import os
import sys
import json
import time
import requests

import urllib

import rw

import json

start = int(time.time())

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

waitFlag = True
showUrl = True

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

# Get list of machines

url = "https://{0}/catalog-service/api/consumer/resources?$filter=resourceType/id eq 'Infrastructure.Virtual' and substringof('sc-power', name)&$orderby=name%20asc&limit=250".format(host)
request = rw.getUrl(url,headers, showUrl=showUrl)

from collections import defaultdict

machines = defaultdict(list)

print request["metadata"]

resourceId = ""

for i in request["content"]:

	machine = i["name"]
	resourceId  = i["id"]

	if ( machine == "sc-powertest-034" ):
		print "Skip "+machine
		continue

	if ( machine == "sc-powertest-219" ):
		print "Skip "+machine
		continue

	if ( machine == "sc-powertest-023" ):
		print "Skip "+machine
		continue

	machines[i["name"]].append(i["id"]) 

	gUrl = ""
	pUrl = ""
	action = ""

	url = "https://{0}/catalog-service/api/consumer/resourceViews/{1}".format(host,resourceId)
	request = rw.getUrl(url,headers, showUrl=showUrl)

	#print machine+" :: "+str(request)

	response = ""

	if 'links' not in request:
		print request
		print machine+" :: No links in response"
		exit(1)

	for c in request['links']:
		#print machine+" : "+c['rel']
		if ("PowerOff" in c['rel']): 
			if ("GET" in c['rel']):
				gUrl=c['href']
			if ("POST" in c['rel']):
				pUrl=c['href']
				action = "Power Off"

		if ("PowerOn" in c['rel']): 
			if ("GET" in c['rel']):
				gUrl=c['href']
			if ("POST" in c['rel']):
				pUrl=c['href']
				action = "Power On"

	print machine+" : resource ID : "+resourceId+" : "+action

	if ( gUrl == "" ):
		print machine+" : No power cycle action found"
		exit(1)

	machines[i["name"]].append(action)	
	machines[i["name"]].append(gUrl)  	
	machines[i["name"]].append(pUrl)	

datacollect = int(time.time())
elapsed = datacollect - start 
print "Elapsed time for data collection : "+str(elapsed)+" seconds"

for name in machines.keys():
	print machines[name][1]+" request for "+name

	gUrl = machines[name][2]
	pUrl = machines[name][3]

	request = rw.getUrl(gUrl,headers, showUrl=False)
	#print name+" : "+json.dumps(request)

	response = rw.postUrl(pUrl, headers, json.dumps(request), showUrl=showUrl)

	#print name+" : "+str(response.headers)

	url = response.headers['Location'] 
	response = rw.getUrl(url,headers,showUrl=showUrl)
	print name+" : Request : "+str(response['requestNumber']),str(response['id']),response['state'],response['phase']
	machines[name].append(url)

while waitFlag:
	for name in machines.keys():

		url = machines[name][4]

		response = rw.getUrl(url,headers,showUrl=False)
		if ( 'phase' not in response ):
			print response
			break
		
		if response['phase'] != "SUCCESSFUL" and response['phase'] != "FAILED" : 
			waitFlag = True
		else:
			print name+" : Request : "+str(response['requestNumber']),str(response['id']),response['state'],response['phase']
			del(machines[name])
			waitFlag = False

	print str(len(machines)) + " requests in progress"
	time.sleep(15) 


end = int(time.time())
elapsed = end - start 
print "Elapsed time : "+str(elapsed)+" seconds"

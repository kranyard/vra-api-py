#!/usr/bin/env python
import operator
import os
import sys
import json
import time
import requests
import datetime
import urllib

from collections import defaultdict

import rw

start = int(time.time())

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

waitFlag = True
showUrl = True

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

maxMachines = sys.argv[1]

skipMachines = [
"sc-powertest-004",
"sc-powertest-034",
"sc-powertest-031",
"sc-powertest-219",
"sc-powertest-023"]

# Get list of machines

url = "https://{0}/catalog-service/api/consumer/resources?$filter=resourceType/id eq 'Infrastructure.Virtual' and substringof('sc-power', name)&$orderby=name%20asc&limit=5000".format(host)
request = rw.getUrl(url,headers, showUrl=showUrl)
print request["metadata"]

machines = defaultdict(list)

resourceId = ""
countMachines = 0

for i in request["content"]:

	machine = i["name"]
	resourceId  = i["id"]

	# Check to see if 'machine' is in 'skipMachines' list
	if (len(filter (lambda x : x == machine, skipMachines)) > 0):
		print "Skip "+machine
		continue
	
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
		continue

	machines[i["name"]].append(i["id"]) 
	machines[i["name"]].append(action)	
	machines[i["name"]].append(gUrl)  	
	machines[i["name"]].append(pUrl)	

	countMachines += 1
	if ( countMachines == int(maxMachines) ):
		break

# Data collection finished

datacollect = int(time.time())

# Submit action requests

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


print "Total machines : "+str(maxMachines)
elapsed = datacollect - start 
print "Elapsed time for data collection : "+str(elapsed)+" seconds "+str(datetime.timedelta(seconds=elapsed))

end = int(time.time())
elapsed = end - start 
print "Total elapsed time : "+str(elapsed)+" seconds "+str(datetime.timedelta(seconds=elapsed))

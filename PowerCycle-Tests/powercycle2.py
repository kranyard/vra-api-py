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

machine = urllib.quote(sys.argv[1])

waitFlag = True
showUrl = True

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/consumer/resources?$filter=name%20eq%20'{1}'".format(host,machine)
request = rw.getUrl(url,headers, showUrl=showUrl)

if 'content' not in request:
	print request
	print machine+" :: No content found"
	exit(1)


if (request["metadata"]["totalElements"] == 0):
	print request
	print machine+" :: Not found"
	exit(1)
	

c = request["content"][0]
resourceId  = c ['id']

print machine+" : resource ID : "+resourceId

gUrl = ""
pUrl = ""

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
			print machine+" : Power Off"

	if ("PowerOn" in c['rel']): 
		if ("GET" in c['rel']):
			gUrl=c['href']
		if ("POST" in c['rel']):
			pUrl=c['href']
			print machine+" : Power On"

if ( gUrl == "" ):
	print machine+" : No power cycle action found"
	exit(1)

request = rw.getUrl(gUrl,headers, showUrl=showUrl)
print machine+" : "+json.dumps(request)


response = rw.postUrl(pUrl, headers, json.dumps(request), showUrl=showUrl)

print machine+" : "+str(response.headers)

url = response.headers['Location'] 
response = rw.getUrl(url,headers,showUrl=False)
print machine+" : Request : "+str(response['requestNumber']),str(response['id']),response['state'],response['phase']

while waitFlag:
	response = rw.getUrl(url,headers,showUrl=False)
	if ( 'phase' not in response ):
		print response
		break
	
	#print response['requestNumber'],response['id'],response['state'],response['phase']
	if response['phase'] == "SUCCESSFUL" or response['phase'] == "FAILED" : 
		print machine+" : Request : "+str(response['requestNumber']),str(response['id']),response['state'],response['phase']
		break
	time.sleep(60) 


end = int(time.time())

elapsed = end - start 

print machine+ " : Elapsed time : "+str(elapsed)+" seconds"

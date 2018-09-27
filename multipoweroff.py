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

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

machine1 = urllib.quote(sys.argv[1])
machine2 = urllib.quote(sys.argv[2])

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/consumer/resources?$filter=name%20eq%20'{1}'".format(host,machine1)
request = rw.getUrl(url,headers)

c = request["content"][0]
resourceId  = c ['id']

gUrl = ""
pUrl = ""

url = "https://{0}/catalog-service/api/consumer/resourceViews/{1}".format(host,resourceId)
request = rw.getUrl(url,headers)

for c in request['links']:
	#print c['rel']
	if ("PowerOn" in c['rel']): 
		if ("GET" in c['rel']):
			gUrl=c['href']
		if ("POST" in c['rel']):
			pUrl=c['href']
		print "Power On : "+machine1

if ( gUrl == "" ):
	print "No power off action found"
	exit(1)

request1 = rw.getUrl(gUrl,headers)
print request1

url = "https://{0}/catalog-service/api/consumer/resources?$filter=name%20eq%20'{1}'".format(host,machine2)
request = rw.getUrl(url,headers)

c = request["content"][0]
resourceId  = c ['id']

gUrl = ""
pUrl = ""

url = "https://{0}/catalog-service/api/consumer/resourceViews/{1}".format(host,resourceId)
request = rw.getUrl(url,headers)

for c in request['links']:
	#print c['rel']
	if ("PowerOn" in c['rel']): 
		if ("GET" in c['rel']):
			gUrl=c['href']
		if ("POST" in c['rel']):
			pUrl=c['href']
		print "Power On : "+machine2

if ( gUrl == "" ):
	print "No power off action found"
	exit(1)

request2 = rw.getUrl(gUrl,headers)
print request2

request = json.dumps(request1)+" "+json.dumps(request2)

response = rw.postUrl(pUrl, headers, request)
print response
url = response.headers['Location'] 
x = rw.getUrl(url,headers,showUrl=False)
print x['requestNumber'],x['id'],x['state'],x['phase']

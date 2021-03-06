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

machine = urllib.quote(sys.argv[1])

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/consumer/resources?$filter=name%20eq%20'{1}'".format(host,machine)
request = rw.getUrl(url,headers)

c = request["content"][0]
resourceId  = c ['id']

gUrl = ""
pUrl = ""

url = "https://{0}/catalog-service/api/consumer/resourceViews/{1}".format(host,resourceId)
request = rw.getUrl(url,headers)

for c in request['links']:
	print c['rel']
	if ("xPowerOff" in c['rel']): 
		if ("GET" in c['rel']):
			gUrl=c['href']
		if ("POST" in c['rel']):
			pUrl=c['href']
		print "Power Off : "+machine

if ( gUrl == "" ):
	print "No power off action found"
	exit(1)

request = rw.getUrl(gUrl,headers)
print request

response = rw.postUrl(pUrl, headers, json.dumps(request))
print response
url = response.headers['Location'] 
x = rw.getUrl(url,headers,showUrl=False)
print x['requestNumber'],x['id'],x['state'],x['phase']

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

machine = urllib.quote("'"+sys.argv[1]+"'")

waitFlag = False

headers = "-H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"".format(id)

url = "https://{0}/catalog-service/api/consumer/resources?$filter=name+eq+'{1}'".format(host,machine)
request = rw.getUrl(url,headers)

c = request["content"][0]
resourceId  = c ['id']

machine = sys.argv[1]

gUrl = ""
pUrl = ""

url = "https://{0}/catalog-service/api/consumer/resourceViews/{1}".format(host,resourceId)
request = rw.getUrl(url,headers)

response = ""

for c in request['links']:
	#print c['rel']
	if ("PowerOff" in c['rel']): 
		if ("GET" in c['rel']):
			gUrl=c['href']
		if ("POST" in c['rel']):
			pUrl=c['href']
		print "Power Off : "+machine

	if ("PowerOn" in c['rel']): 
		if ("GET" in c['rel']):
			gUrl=c['href']
		if ("POST" in c['rel']):
			pUrl=c['href']
		print "Power On : "+machine

if ( gUrl == "" ):
	print "No action found"
	exit(1)

request = rw.getUrl(gUrl,headers)
#print request

data = "\'{0}\'".format(json.dumps(request))
response = rw.postUrl(pUrl, headers, data=data)

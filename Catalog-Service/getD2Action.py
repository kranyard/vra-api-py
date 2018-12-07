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

showUrl = False

machine = urllib.quote(sys.argv[1])
action = sys.argv[2]

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/consumer/resources?$filter=name%20eq%20'{1}'".format(host,machine)
request = rw.getUrl(url,headers, showUrl=showUrl)

c = request["content"][0]
this_id = c ['id']

url = "https://{0}/catalog-service/api/consumer/resourceViews/{1}".format(host,this_id)
request = rw.getUrl(url,headers, showUrl=showUrl)

#print json.dumps(request)

for c in request['links']:
	#print c['rel']
	if (action in c['rel']): 
		if ("GET" in c['rel']):
			gUrl=c['href']
		if ("POST" in c['rel']):
			pUrl=c['href']

request = rw.getUrl(gUrl,headers, showUrl=showUrl)

print json.dumps(request)

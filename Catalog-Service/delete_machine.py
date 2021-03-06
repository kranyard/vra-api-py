#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import rw

import urllib
import json

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

machine = urllib.quote(sys.argv[1])
action = "estroy"

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/consumer/resources?$filter=name%20eq%20'{1}'".format(host,machine)
request = rw.getUrl(url,headers)

c = request["content"][0]
this_id = c ['id']

tenantLabel=c['organization']['tenantLabel']
tenantRef=c['organization']['tenantRef']
subtenantLabel=c['organization']['subtenantLabel']
subtenantRef=c['organization']['subtenantRef']

url = "https://{0}/catalog-service/api/consumer/resourceViews/{1}".format(host,this_id)
request = rw.getUrl(url,headers)

#print json.dumps(request)

for c in request['links']:
	print c['rel']
	if (action in c['rel']): 
		if ("GET" in c['rel']):
			gUrl=c['href']
		if ("POST" in c['rel']):
			pUrl=c['href']
	
request = rw.getUrl(gUrl,headers)

rw.postUrl(pUrl, headers, json.dumps(request))


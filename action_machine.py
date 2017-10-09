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
action = sys.argv[2]

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/consumer/resources?$filter=name%20eq%20'{1}'".format(host,machine)
request = rw.getUrl(url,headers)

c = request["content"][0]
this_id = c ['id']

parent = c['parentResourceRef']
parent_id = parent['id']

tenantLabel=c['organization']['tenantLabel']
tenantRef=c['organization']['tenantRef']
subtenantLabel=c['organization']['subtenantLabel']
subtenantRef=c['organization']['subtenantRef']

url = "https://{0}/catalog-service/api/consumer/resources/{1}/actions".format(host,parent_id)
request = rw.getUrl(url,headers)

print parent['label']
for c in request['content']:
	print "  ",c['name']

parent_id = parent['id']

url = "https://{0}/catalog-service/api/consumer/resources/{1}/actions".format(host,this_id)
request = rw.getUrl(url,headers)

print machine
for c in request['content']:
	print "  ",c['name']

for c in request['content']:
	if c['name'] == action : 
		resourceActionRef=c['id']

		action_payload={"@type":"ResourceActionRequest","resourceRef":{"id":this_id }, "resourceActionRef":{"id":resourceActionRef}, "organization":{"tenantRef":tenantRef,"tenantLabel":tenantLabel,"subtenantRef":subtenantRef,"subtenantLabel":subtenantLabel },"state":"SUBMITTED", "requestNumber":0, "requestData":{"entries":[{"key":"description", "value":{"type":"string" , "value":"test"}},{"key":"reasons"}]}}

		url = "https://{0}/catalog-service/api/consumer/requests".format(host)
		r=rw.postUrl(url,headers=headers,data=json.dumps(action_payload))

		r=rw.getUrl(r.headers['Location'],headers=headers)

		print r

		exit(0)

print "No action found"


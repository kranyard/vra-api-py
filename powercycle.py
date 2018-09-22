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

tenantLabel=c['organization']['tenantLabel']
tenantRef=c['organization']['tenantRef']
subtenantLabel=c['organization']['subtenantLabel']
subtenantRef=c['organization']['subtenantRef']

url = "https://{0}/catalog-service/api/consumer/resources/{1}/actions".format(host,resourceId)
request = rw.getUrl(url,headers)

print machine

response = ""

for c in request['content']:
	if c['name'] == "Power Off" : 
		resourceActionRef=c['id']
		print "Power off action ref : ",resourceActionRef

		action_payload={"@type":"ResourceActionRequest","resourceRef":{"id":resourceId }, "resourceActionRef":{"id":resourceActionRef}, "organization":{"tenantRef":tenantRef,"tenantLabel":tenantLabel,"subtenantRef":subtenantRef,"subtenantLabel":subtenantLabel },"state":"SUBMITTED", "requestNumber":0, "requestData":{"entries":[{"key":"description", "value":{"type":"string" , "value":"Test Auto Power Off"}},{"key":"reasons"}]}}

		url = "https://{0}/catalog-service/api/consumer/requests".format(host)
		response=rw.postUrl(url,headers=headers,data=json.dumps(action_payload))
		url = response.headers['Location'] 


	if c['name'] == "Power On" : 
		resourceActionRef=c['id']
		print "Power on action ref : ",resourceActionRef

		action_payload={"@type":"ResourceActionRequest","resourceRef":{"id":resourceId }, "resourceActionRef":{"id":resourceActionRef}, "organization":{"tenantRef":tenantRef,"tenantLabel":tenantLabel,"subtenantRef":subtenantRef,"subtenantLabel":subtenantLabel },"state":"SUBMITTED", "requestNumber":0, "requestData":{"entries":[{"key":"description", "value":{"type":"string" , "value":"Test Auto Power On"}},{"key":"reasons"}]}}

		url = "https://{0}/catalog-service/api/consumer/requests".format(host)
		response=rw.postUrl(url,headers=headers,data=json.dumps(action_payload))
		print response
		url = response.headers['Location'] 

while True:
	x = rw.getUrl(url,headers,showUrl=False)
	print x['requestNumber'],x['id'],x['state'],x['phase']
	if x['phase'] == "SUCCESSFUL" : 
		break
	time.sleep(10) 


#!/usr/bin/env python
import operator
import os
import sys
import json

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

machine = sys.argv[1]
action = sys.argv[2]

headers = "-H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"".format(id)
url = "https://{0}//catalog-service/api/consumer/resources?limit=99999".format(host)
request = rw.getUrl(url, headers, showUrl=True) 
print json.dumps(request)

parent = None 

for x in request["content"]:
	if (x['name'] == machine ):
		this_id = x ['id']
		parent = x['parentResourceRef']
		tenantLabel=x['organization']['tenantLabel']
		tenantRef=x['organization']['tenantRef']
		subtenantLabel=x['organization']['subtenantLabel']
		subtenantRef=x['organization']['subtenantRef']

if ( parent == None ):
	print "Machine ["+machine+"] not found"
	exit(1)


parent_id = parent['id']

url = "https://{0}/catalog-service/api/consumer/resources/{1}/actions".format(host,this_id)
request = rw.getUrl(url, headers, showUrl=True) 

print json.dumps(request)

for c in request['content']:
	if c['name'] == action : 
		resourceActionRef=c['id']

		action_payload={"@type":"ResourceActionRequest","resourceRef":{"id":this_id }, "resourceActionRef":{"id":resourceActionRef}, "organization":{"tenantRef":tenantRef,"tenantLabel":tenantLabel,"subtenantRef":subtenantRef,"subtenantLabel":subtenantLabel },"state":"SUBMITTED", "requestNumber":0, "requestData":{"entries":[{"key":"description", "value":{"type":"string" , "value":"test"}},{"key":"reasons"}]}}

		url=https://{0}/catalog-service/api/consumer/requests".format(host)
		data = "\'{0}\'".format(json.dumps(action_payload))

		request = rw.postUrl(url, headers, data, showUrl=True)

		exit(0)

print "No action found"


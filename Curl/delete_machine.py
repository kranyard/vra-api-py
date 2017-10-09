#!/usr/bin/env python
import operator
import os
import sys
import json

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

machine = sys.argv[1]

cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"  https://{1}/catalog-service/api/consumer/resources?limit=99999 2> /dev/null".format(id,host)

stream = os.popen(cmd)

request = json.loads(stream.read())

#print json.dumps(request)

parent = None 

for x in request["content"]:
	if (x['name'] == machine ):
		parent = x['parentResourceRef']
		print "Delete RESOURCE ID",parent['id'],parent['label'],

		tenantLabel=x['organization']['tenantLabel']
		tenantRef=x['organization']['tenantRef']
		subtenantLabel=x['organization']['subtenantLabel']
		subtenantRef=x['organization']['subtenantRef']

if ( parent == None ):
	print "Machine ["+machine+"] not found"
	exit(1)

parent_id = parent['id']

cmd="curl --insecure -H \"Accept: application/json;charset=UTF-8\" -H \"Content-Type: application/json;charset=UTF-8\" -H \"Authorization: Bearer {0} \"  https://{1}/catalog-service/api/consumer/resources/{2}/actions 2> /dev/null".format(id,host,parent_id)

stream = os.popen(cmd)

request = json.loads(stream.read())

for c in request['content']:
	print c['name']
	if c['name'] == "Destroy" : 
		resourceActionRef=c['id']

exit(1)

delete_json={"@type":"ResourceActionRequest","resourceRef":{"id":parent_id }, "resourceActionRef":{"id":resourceActionRef}, "organization":{"tenantRef":tenantRef,"tenantLabel":tenantLabel,"subtenantRef":subtenantRef,"subtenantLabel":subtenantLabel },"state":"SUBMITTED", "requestNumber":0, "requestData":{"entries":[]}}

cmd="curl --verbose --insecure -X POST -H \"Accept: application/json;charset=UTF-8\" -H \"Content-Type: application/json;charset=UTF-8\" -H \"Authorization: Bearer {0} \"  --data \'{2}\' https://{1}/catalog-service/api/consumer/requests 2> /dev/null".format(id,host,json.dumps(delete_json))

stream = os.popen(cmd)


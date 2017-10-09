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

cmd="curl --insecure -H \"Accept: application/json;charset=UTF-8\" -H \"Content-Type: application/json;charset=UTF-8\" -H \"Authorization: Bearer {0} \"  https://{1}/catalog-service/api/consumer/resources/{2}/actions 2> /dev/null".format(id,host,parent_id)

stream = os.popen(cmd)

request = json.loads(stream.read())

print parent['label']
for c in request['content']:
	print "  ",c['name']

cmd="curl --insecure -H \"Accept: application/json;charset=UTF-8\" -H \"Content-Type: application/json;charset=UTF-8\" -H \"Authorization: Bearer {0} \"  https://{1}/catalog-service/api/consumer/resources/{2}/actions 2> /dev/null".format(id,host,this_id)

stream = os.popen(cmd)

request = json.loads(stream.read())

print machine
for c in request['content']:
	print "  ",c['name']

#!/usr/bin/env python
import operator
import os
import sys
import json

debug = False

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \" https://{1}/content-management-service/api/packages 2> /dev/null".format(id,host)

stream = os.popen(cmd)

request = json.loads(stream.read())

if ( debug ):
	print json.dumps(request)
	exit (0)

for item in request['content']:
	for key, value in item.items():
		print key, ':=', value
	print '-----'

for item in request['links']:
	for key, value in item.items():
		print key, ':=', value
	print '-----'

item=request['metadata'] 
for key, value in item.items():
	print key, ':=', value
print '-----'


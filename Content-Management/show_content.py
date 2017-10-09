#!/usr/bin/env python
import operator
import os
import sys
import json

debug = False

cid = sys.argv[1]

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"  https://{1}/content-management-service/api/contents/{2} 2> /dev/null".format(id,host,cid)

stream = os.popen(cmd)

request = json.loads(stream.read())

if ( debug ):
	print json.dumps(request)
	exit (0)

item=request 
for key, value in item.items():
	print key, ':=', value
print '-----'

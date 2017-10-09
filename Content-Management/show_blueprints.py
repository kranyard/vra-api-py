#!/usr/bin/env python
import operator
import os
import sys
import json

debug = False

#docid = sys.argv[1]

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

#cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"  https://{1}/composition-service/api/blueprintdocuments/{2} 2> /dev/null".format(id,host,docid)
cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"  https://{1}/composition-service/api/blueprints 2> /dev/null".format(id,host)

stream = os.popen(cmd)

request = json.loads(stream.read())

if ( debug ):
	print json.dumps(request)
	exit (0)

for item in request['content']:
	for key, value in item.items():
		print key, ':=', value
	print '-----'

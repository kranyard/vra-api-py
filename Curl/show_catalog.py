#!/usr/bin/env python
import operator
import os
import sys
import json


debug = False

if (len(sys.argv) > 1 ):
	debug = True

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"  https://{1}/catalog-service/api/consumer/entitledCatalogItemViews 2> /dev/null".format(id,host)


stream = os.popen(cmd)

request = json.loads(stream.read())

if ( debug ):
	print json.dumps(request)
	exit (0)

print cmd

for item in request['content']:
	print "CATALOG",item['catalogItemId']+"	"+item['name']
	#for key, value in item.items():
		#print key, ':=', value
	#print '-----'

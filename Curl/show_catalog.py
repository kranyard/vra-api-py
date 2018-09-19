#!/usr/bin/env python
import operator
import os
import sys
import json

import rw

debug = False

if (len(sys.argv) > 1 ):
	debug = True

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = "-H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"".format(id)
url = "https://{0}/catalog-service/api/consumer/entitledCatalogItemViews".format(host)
request = rw.getUrl(url, headers, showUrl=True) 

if ( debug ):
	print json.dumps(request)
	exit (0)

for item in request['content']:
	print "CATALOG",item['catalogItemId']+"	"+item['name']
	#for key, value in item.items():
		#print key, ':=', value
	#print '-----'

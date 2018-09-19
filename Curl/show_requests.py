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

url="https://{0}/catalog-service/api/consumer/requests?limit=30&$orderby=requestNumber%20desc".format(host)
request = rw.getUrl(url,headers)

for x in request["content"]:
	print x['id'],x['requestNumber'],x['phase'],x['@type']
	#rw.showProperties(x)


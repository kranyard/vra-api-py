#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json
import pprint

sys.path.append("../")
import rw

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

pp = pprint.PrettyPrinter(indent=4)

debug = False

catId = sys.argv[1]

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/consumer/entitledCatalogItems/{1}".format(host,catId)
request = rw.getUrl(url,headers)

print request['catalogItem']['name']

url = "https://{0}/catalog-service/api/consumer/entitledCatalogItems/{1}/requests/schema".format(host,catId)
request = rw.getUrl(url,headers)

if ( debug ):
	#pp.pprint(request)
	print json.dumps(request)
	exit (0)

for f in request["fields"][1]["dataType"]["schema"]["fields"]:
	if f['id'] == "storage":
		print f['id']
		print "Max Storage : "+str(f['state']['facets'][0]['value']['value']['value'])+"Gb"

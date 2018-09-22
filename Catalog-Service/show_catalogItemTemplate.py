#!/usr/bin/env python
import operator
import os
import sys
import json
import time
import datetime

import json
import pprint

sys.path.append("../")
import rw

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

pp = pprint.PrettyPrinter(indent=4)

debug = True

catId = sys.argv[1]

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

url = "https://{0}/catalog-service/api/consumer/entitledCatalogItems/{1}".format(host,catId)
request = rw.getUrl(url,headers)

print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print request['catalogItem']['name']

url = "https://{0}/catalog-service/api/consumer/entitledCatalogItems/{1}/requests/template".format(host,catId)
request = rw.getUrl(url,headers)

print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if ( debug ):
	#pp.pprint(request)
	print json.dumps(request)

print "---"
url = "https://{0}/catalog-service/api/consumer/entitledCatalogItems/{1}/requests/template?businessGroupId=35c6bdbf-e697-445b-8416-30819929536f".format(host,catId)
request = rw.getUrl(url,headers)

print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if ( debug ):
	#pp.pprint(request)
	print json.dumps(request)

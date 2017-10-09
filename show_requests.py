#!/usr/bin/env python
import operator
import os
import sys
import json

import rw

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url="https://{0}/catalog-service/api/consumer/requests?limit=30&$orderby=requestNumber%20desc".format(host)
request = rw.getUrl(url,headers)

for x in request["content"]:
	print "REQUEST",x['id'],x['requestNumber'],x['phase'],x['@type']
	#for key, value in x.items():
		#print key, ':=', value
	#print '-----'


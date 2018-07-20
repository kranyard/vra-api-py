#!/usr/bin/env python
import operator
import os
import sys
import json

sys.path.append("../")
import rw

debug = False

docid = sys.argv[1]

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/composition-service/api/blueprints/{1}".format(host,docid)

request = rw.getUrl(url,headers)

if ( debug ):
	print json.dumps(request)
	exit (0)

#rw.showProperties(request)

for i in request['components']:
	print i
	print "Memory default value : "+str(request['components'][i]['data']['memory']['facets']['defaultValue']['value']['value'])
	print "Storage default value : "+str(request['components'][i]['data']['storage']['facets']['defaultValue']['value']['value'])
	print "CPU default value : "+str(request['components'][i]['data']['cpu']['facets']['defaultValue']['value']['value'])


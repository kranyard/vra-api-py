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

url = "https://{0}/composition-service/api/blueprints/{1} ".format(host,docid)

request = rw.getUrl(url,headers)

if ( debug ):
	print json.dumps(request)
	exit (0)


rw.showProperties(request)

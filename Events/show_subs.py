#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json
import pprint

import rw

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

pp = pprint.PrettyPrinter(indent=4)

debug = False

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/event-broker-service/api/subscriptions/active".format(host)

request = rw.getUrl(url,headers)

if ( debug ):
	pp.pprint(request)
	#print json.dumps(request)
	exit (0)

for item in request['content']:
	if (True):
		for key, value in item.items():
			if isinstance(value, dict):
				for k, v in value.items():	
					print "  ",k,"::=",v
			elif isinstance(value, list):
				print "list"
				for v in value:	
					print v
			else:
				print key, ':=', value
		print '-----'

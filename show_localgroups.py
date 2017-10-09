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

group = "Content@vsphere.local"
tenant = "vsphere.local"

pp = pprint.PrettyPrinter(indent=4)

debug = False

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/identity/api/tenants/{1}/groups/assigned?criteria={2}".format(host,tenant,group)

request = rw.getUrl(url,headers)

if ( debug ):
	pp.pprint(request)
	#print json.dumps(request)
	exit (0)

for item in request['content']:
	print "User "+item['name']
	if (True):
		for key, value in item.items():
			if isinstance(value, dict):
				print "*DICTIONARY"
				for k, v in value.items():	
					print "  ",k,"::=",v
			elif isinstance(value, list):
				print "*LIST"
				for v in value:	
					print v
			else:
				print key, ':=', value
		print '-----'

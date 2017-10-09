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

url = "https://{0}/identity/api/tenants/vsphere.local/groups/onboard@vsphere.local".format(host)
request = rw.getUrl(url,headers)

#pp.pprint(request)
print json.dumps(request)
 
url = "https://{0}/identity/api/tenants/vsphere.local/groups/?parentGroup=onboard@vsphere.local&page=1&limit=214748364".format(host)
request = rw.getUrl(url,headers)

#pp.pprint(request)
print json.dumps(request)

url = "https://{0}/identity/api/tenants/vsphere.local/principals/?parentGroup=onboard@vsphere.local&page=1&limit=2147483647".format(host)
request = rw.getUrl(url,headers)

#pp.pprint(request)
print json.dumps(request)

exit(0)

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

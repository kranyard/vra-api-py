#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json
import pprint

import rw

import urllib

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

tenant = "vsphere.local"
tenant = "Cava"

group = "Cava-DUpton%20%28Cava-DUpton%40cava%29%40Cava"
group = urllib.quote("Cava-DUpton (Cava-DUpton@cava)@Cava")

pp = pprint.PrettyPrinter(indent=4)

debug = False

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}


url = "https://{0}/identity/api/tenants/{1}/groups/{2}".format(host,tenant,group)
request = rw.getUrl(url,headers)
print "Group :",request['name']


url = "https://{0}/identity/api/tenants/{1}/groups/?parentGroup={2}&page=1&limit=2147483647".format(host,tenant,group)
request = rw.getUrl(url,headers)
print "Parent Groups ::"
if 'content' in request:
	for item in request['content']:
		print "  "+item['name']
else:
	print json.dumps(request)

url = "https://{0}/identity/api/tenants/{1}/groups/{2}/parents/?$top=2147483647&$skip=0&groupType=CUSTOM".format(host,tenant,group)
request = rw.getUrl(url,headers)
print "Groups ::"
for item in request['content']:
	print "  "+item['name']


url = "https://{0}/identity/api/tenants/{1}/principals/?parentGroup={2}&page=1&limit=2147483647".format(host,tenant,group)
request = rw.getUrl(url,headers)

print "Principals ::"
if 'content' in request:
	for value in request['content']:
		if 'emailAddress' in value:
			print "  ",value['name']," [",value['emailAddress']," ]"
		else:
			print "  ",value['name']

	print '-----'
else:
	print json.dumps(request)
	

if False:
	if isinstance(value, dict):
		print "**DICT"
		for k, v in value.items():	
			print "  ",k,"::=",v
	elif isinstance(value, list):
		print "**LIST"
		for v in value:	
			print v
	else:
		#print value," :::- ",request[value]
		print value
	
	print '-----'


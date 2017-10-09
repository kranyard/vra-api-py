#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import urllib

import json
import pprint

import rw

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

tenant = "vsphere.local"
tenant = "Cava"

pp = pprint.PrettyPrinter(indent=4)

debug = False

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/identity/api/tenants/{1}/groups/?groupType=CUSTOM&limit=9999".format(host,tenant)
request = rw.getUrl(url,headers)
for item in request['content']:

	group = urllib.quote(item['name']+"@"+tenant)

	url = "https://{0}/identity/api/tenants/{1}/groups/{2}".format(host,tenant,group)
	request = rw.getUrl(url,headers)
	print "Group :",request['name']


	url = "https://{0}/identity/api/tenants/{1}/groups/{2}/parents/?$top=2147483647&$skip=0&groupType=CUSTOM".format(host,tenant,group)
	request = rw.getUrl(url,headers)
	print "Parent Groups ::"
	for item in request['content']:
		print "  "+item['name']

	url = "https://{0}/identity/api/tenants/{1}/groups/?parentGroup={2}&page=1&limit=2147483647".format(host,tenant,group)
	request = rw.getUrl(url,headers)
	print "Groups ::"
	for item in request['content']:
		print "  "+item['name']

	url = "https://{0}/identity/api/tenants/{1}/principals/?parentGroup={2}&page=1&limit=2147483647".format(host,tenant,group)
	request = rw.getUrl(url,headers)

	print "Principals ::"
	for value in request['content']:
		if 'emailAddress' in value:
			print "  ",value['name']," [",value['emailAddress']," ]"
		else:
			print "  ",value['name']

	print '-----'

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


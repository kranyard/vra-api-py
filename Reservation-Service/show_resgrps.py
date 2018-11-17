#!/usr/bin/env python
import operator
import os
import sys
import json

sys.path.append("../")
import rw

login = False 

if (login):
	# Define hostname and credentials
	host="vra-01a.corp.local"
	username="jason@corp.local"
	tenant="vsphere.local"
	password="VMware1!"

	values = { 'username':username, 'password':password, 'tenant':tenant }
	data = json.dumps(values)
	headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8'}

	r=rw.postUrl("https://{0}/identity/api/tokens".format(host),data=data,headers=headers)

	resp = r.json()

	# Extract ID token from JSON payload response from vRA
	id = resp["id"]
else:
	host = os.environ['VRAHOST']
	id = os.environ['VRATOKEN']

debug = False

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url="https://{0}/reservation-service/api/reservations/policies".format(host)
request = rw.getUrl(url,headers)

if ( debug ):
	print json.dumps(request)
	exit (0)

for item in request['content']:
	print "RESERVATION POLICY",item['name']+"    "+item['id']
	#for key, value in item.items():
	#	print key, ':=', value
	#print '-----'

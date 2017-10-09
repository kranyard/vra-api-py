#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import rw

host="vra-01a.corp.local"
username="jason@corp.local"
tenant="vsphere.local"
password="VMware1!"

Debug = True

request_id=sys.argv[1]

values = { 'username':username, 'password':password, 'tenant':tenant }
data = json.dumps(values)

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8'}

url = "https://{0}/identity/api/tokens".format(host)

r = rw.postUrl(url,headers,data,showUrl=False)

request = r.json()

#print request[0]['expires']

id = request['id']

print "Request ID :",request_id

url= "https://{0}/catalog-service/api/consumer/requests/{1}/resourceViews".format(host,request_id)

r = rw.getUrl(url,headers,showUrl=False)

for c in r["content"]: 
	print "Component:",c["name"]

	if ( Debug ) :
		for key, value in c.items():
			print key, ':=', value
		print '-----'

	if ( c["hasChildren"] == True ):
		# This is parent component
		print ("Description: "+c["description"])

	if 'data' in c:
		if 'ip_address' in c["data"]:
			print "   IP address:",c["data"]["ip_address"]

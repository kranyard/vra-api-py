#!/usr/bin/env python
import operator
import os
import sys
import json
import time

request_id=sys.argv[1]

# Define hostname and credentials
host="vra-01a.corp.local"
username="jason@corp.local"
tenant="vsphere.local"
password="VMware1!"

# Build curl cmd using credentials etc
cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" --data \'{{\"username\":\"{0}\",\"password\":\"{1}\",\"tenant\":\"{2}\"}}\' https://{3}/identity/api/tokens 2> /dev/null".format(username,password,tenant,host)

# Create pipe to execute curl cmd
stream = os.popen(cmd)

# Read JSON payload as response from vRA
id_json = json.loads(stream.read())

id = id_json["id"] 

cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"  https://{1}/catalog-service/api/consumer/requests/{2} 2> /dev/null".format(id,host,request_id)

stream = os.popen(cmd)
x = json.loads(stream.read())
print x['requestNumber'],x['id'],x['state'],x['phase']

cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"  https://{1}/catalog-service/api/consumer/requests/{2}/resourceViews 2> /dev/null".format(id,host,request_id)

stream = os.popen(cmd)
request = json.loads(stream.read())

#print json.dumps(request) 

c=request["content"]

for c in request["content"]: 
	#for key, value in c.items():
		#print key, ':=', value
	#print '-----'
	print c["name"]
	if 'data' in c:
		if 'ip_address' in c["data"]:
			print "   ",c["data"]["ip_address"]

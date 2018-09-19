#!/usr/bin/env python
import operator
import os
import sys
import json

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

machine = sys.argv[1]

headers = "-H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"".format(id)
url = "https://{0}//catalog-service/api/consumer/resources?limit=99999".format(host)
request = rw.getUrl(url, headers, showUrl=True) 
#print json.dumps(request)

parent = None 

for x in request["content"]:
	if (x['name'] == machine ):
		this_id = x ['id']
		parent = x['parentResourceRef']
		tenantLabel=x['organization']['tenantLabel']
		tenantRef=x['organization']['tenantRef']
		subtenantLabel=x['organization']['subtenantLabel']
		subtenantRef=x['organization']['subtenantRef']

if ( parent == None ):
	print "Machine ["+machine+"] not found"
	exit(1)


parent_id = parent['id']

url = "https://{0}/catalog-service/api/consumer/resources/{1}/actions".format(host,parent_id)
request = rw.getUrl(url, headers, showUrl=True) 

print parent['label']
for c in request['content']:
	print "  ",c['name']

url = "https://{0}/catalog-service/api/consumer/resources/{1}/actions".format(host,this_id)
request = rw.getUrl(url, headers, showUrl=True) 

print machine
for c in request['content']:
	print "  ",c['name']

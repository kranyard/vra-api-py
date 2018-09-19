#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import rw

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = "-H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"".format(id)

url="https://{0}/catalog-service/api/consumer/requests?limit=30&$orderby=requestNumber%20desc".format(host)
request = rw.getUrl(url,headers, showUrl=True)

i=0
for x in request["content"]:
	i+=1
	print i,"REQUEST",x['id'],x['requestNumber'],x['phase']

select=input("Enter request number ")
print select, request['content'][select-1]['id']

request_id=request['content'][select-1]['id']

url = "https://{0}/catalog-service/api/consumer/requests/{1}".format(host,request_id)

while True:
	x = rw.getUrl(url, headers, showUrl=True) 
	print x['requestNumber'],x['id'],x['state'],x['phase']
	if x['phase'] == "SUCCESSFUL" : 
		break
	time.sleep(10) 

url = "https://{0}/catalog-service/api/consumer/requests/{1}/resourceViews".format(host,request_id)
request = rw.getUrl(url, headers, showUrl=True) 

print json.dumps(request) 

c=request["content"]

for c in request["content"]: 
	print c["name"]
	if 'data' in c:
		if 'ip_address' in c["data"]:
			print "   ",c["data"]["ip_address"]

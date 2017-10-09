#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import rw

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url="https://{0}/catalog-service/api/consumer/requests?limit=30&$orderby=requestNumber%20desc".format(host)
request = rw.getUrl(url,headers)

#cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"  https://{1}/catalog-service/api/consumer/requests?limit=99999 2> /dev/null".format(id,host)
#stream = os.popen(cmd)
#request = json.loads(stream.read())

i=0
for x in request["content"]:
	i+=1
	print i,"REQUEST",x['id'],x['requestNumber'],x['phase']

select=input("Enter request number ")
print select, request['content'][select-1]['id']

request_id=request['content'][select-1]['id']

cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"  https://{1}/catalog-service/api/consumer/requests/{2} 2> /dev/null".format(id,host,request_id)

while True:
	stream = os.popen(cmd)
	x = json.loads(stream.read())
	print x['requestNumber'],x['id'],x['state'],x['phase']
	if x['phase'] == "SUCCESSFUL" : 
		break
	time.sleep(10) 

cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"  https://{1}/catalog-service/api/consumer/requests/{2}/resourceViews 2> /dev/null".format(id,host,request_id)

stream = os.popen(cmd)

request = json.loads(stream.read())

#print json.dumps(request) 

c=request["content"]

for c in request["content"]: 
	print c["name"]
	if 'data' in c:
		if 'ip_address' in c["data"]:
			print "   ",c["data"]["ip_address"]

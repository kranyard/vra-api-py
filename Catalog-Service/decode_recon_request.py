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

i=0
for x in request["content"]:
	i+=1
	print i,"REQUEST",x['id'],x['requestNumber'],x['phase']

select=input("Enter request number ")
print select, request['content'][select-1]['id']

request_id=request['content'][select-1]['id']

url="https://{0}/catalog-service/api/consumer/requests/{1}".format(host,request_id)
res = rw.getUrl(url,headers)

e = res['requestData']['entries']

for i in e:
	print json.dumps(i)

#	if ( i['key'] == "provider-Cafe.Shim.VirtualMachine.Reconfigure.UpdatedMemorySize" ):
#	if ( i['key'] == "provider-Cafe.Shim.VirtualMachine.Reconfigure.UpdatedTotalStorageSize" ):
#	if ( i['key'] == "provider-Cafe.Shim.VirtualMachine.Reconfigure.UpdatedCpuCount" ):
#	if ( i['key'] == "provider-Cafe.Shim.VirtualMachine.Reconfigure.MemorySize" ):


print "Requested For : ",res['requestedFor']
print "Requested By : ",res['requestedBy']

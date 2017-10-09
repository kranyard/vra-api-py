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

url="https://{0}/catalog-service/api/consumer/entitledCatalogItemViews".format(host)
request = rw.getUrl(url,headers)

i=0
for item in request['content']:
	i+=1
	print i,item['catalogItemId'],item['name']

select=input("Enter catalog number ")
print select, request['content'][select-1]['name']

select_id=request['content'][select-1]['catalogItemId']
print select_id

url="https://{0}/catalog-service/api/consumer/entitledCatalogItems/{1}/requests/template".format(host,select_id)
request = rw.getUrl(url,headers)

#print json.dumps(request)

url="https://{0}/catalog-service/api/consumer/entitledCatalogItems/{1}/requests".format(host,select_id)
r=rw.postUrl(url,headers=headers,data=json.dumps(request))

request = r.json()

#print json.dumps(request)
request_id = request['id']

url="https://{0}/catalog-service/api/consumer/requests/{1}".format(host,request_id)

while True:
	x = rw.getUrl(url,headers,showUrl=True)
	print x['requestNumber'],x['id'],x['state'],x['phase']
	time.sleep(10) 
	if x['phase'] == "SUCCESSFUL" : 
		break

url="https://{0}/catalog-service/api/consumer/requests/{1}/resourceViews".format(host,request_id)
request = rw.getUrl(url,headers)

print json.dumps(request) 

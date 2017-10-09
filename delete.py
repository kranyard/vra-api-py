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

url="https://{0}/catalog-service/api/consumer/resources?limit=99999".format(host)
request = rw.getUrl(url,headers)

i=0
for item in request['content']:
	i+=1
	print i,"RESOURCE",item['id'],item['name']

select=input("Enter resource number ")
#print select, request['content'][select-1]['id']

resource_id = request['content'][select-1]['id']

tenantLabel=request['content'][select-1]['organization']['tenantLabel']
tenantRef=request['content'][select-1]['organization']['tenantRef']
subtenantLabel=request['content'][select-1]['organization']['subtenantLabel']
subtenantRef=request['content'][select-1]['organization']['subtenantRef']

url="https://{0}/catalog-service/api/consumer/resources/{1}/actions".format(host,resource_id)
request = rw.getUrl(url,headers)

for c in request['content']:
	if c['name'] == "Destroy" : 
		resourceActionRef=c['id']


delete_json={"@type":"ResourceActionRequest","resourceRef":{"id":resource_id }, "resourceActionRef":{"id":resourceActionRef}, "organization":{"tenantRef":tenantRef,"tenantLabel":tenantLabel,"subtenantRef":subtenantRef,"subtenantLabel":subtenantLabel },"state":"SUBMITTED", "requestNumber":0, "requestData":{"entries":[]}}

url="https://{0}/catalog-service/api/consumer/requests".format(host)
r=rw.postUrl(url,headers=headers,data=json.dumps(delete_json))

r=rw.getUrl(r.headers['Location'],headers=headers)

print r

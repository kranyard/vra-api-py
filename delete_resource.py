#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import rw

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

#request_id=raw_input("Enter request ID : ")
request_id = sys.argv[1]

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url="https://{0}/catalog-service/api/consumer/requests/{1}".format(host,request_id)
request = rw.getUrl(url,headers)

print "REQUEST",request['requestNumber'],request['id'],request['phase']

url="https://{0}/catalog-service/api/consumer/requests/{1}/resourceViews".format(host,request_id)
request = rw.getUrl(url,headers)

#print json.dumps(request) 

for c in request["content"]:
	if c["hasChildren"]:
		print "PARENT",c["resourceId"], c["name"]
		resource_id = c["resourceId"]
	else:
		print "CHILD",c["resourceId"], c["name"]

url="https://{0}/catalog-service/api/consumer/resources/{1}".format(host,resource_id)
item = rw.getUrl(url,headers)

print "RESOURCE",item['id'],item['name']

tenantLabel=item['organization']['tenantLabel']
tenantRef=item['organization']['tenantRef']
subtenantLabel=item['organization']['subtenantLabel']
subtenantRef=item['organization']['subtenantRef']

url="https://{0}/catalog-service/api/consumer/resources/{1}/actions".format(host,resource_id)
request = rw.getUrl(url,headers)

for c in request['content']:
	if c['name'] == "Destroy" : 
		resourceActionRef=c['id']


delete_json={"@type":"ResourceActionRequest","resourceRef":{"id":resource_id }, "resourceActionRef":{"id":resourceActionRef}, "organization":{"tenantRef":tenantRef,"tenantLabel":tenantLabel,"subtenantRef":subtenantRef,"subtenantLabel":subtenantLabel },"state":"SUBMITTED", "requestNumber":0, "requestData":{"entries":[]}}

url = "https://{0}/catalog-service/api/consumer/requests".format(host)
r=rw.postUrl(url,headers=headers,data=json.dumps(delete_json))

r=rw.getUrl(r.headers['Location'],headers=headers)
print r

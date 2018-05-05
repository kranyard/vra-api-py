#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json

import rw

import urllib

deployment = urllib.quote(sys.argv[1])

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

#host="vra-01a.corp.local"
#username="jason@corp.local"
#tenant="vsphere.local"
#password="VMware1!"

#values = { 'username':username, 'password':password, 'tenant':tenant }
#data = json.dumps(values)
#headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8'}

#r=rw.postUrl("https://{0}/identity/api/tokens".format(host),data=data,headers=headers)

#resp = r.json()

#id = resp["id"]

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

#url = "https://{0}/catalog-service/api/consumer/resources?$filter=requestNumber%20eq%20{1}".format(host,request_number)
url = "https://{0}/catalog-service/api/consumer/resources?$filter=name%20eq%20'{1}'&limit=9999".format(host,deployment)
request = rw.getUrl(url,headers)

#print json.dumps(request)

request_id = request['content'][0]['requestId']

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

url="https://{0}/catalog-service/api/consumer/requests".format(host)
r=rw.postUrl(url,headers=headers,data=json.dumps(delete_json))

r=rw.getUrl(r.headers['Location'],headers=headers)

print r

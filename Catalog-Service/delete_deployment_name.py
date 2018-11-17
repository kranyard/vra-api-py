#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import rw

import urllib

deployment = urllib.quote(sys.argv[1])

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/consumer/resources?$filter=name%20eq%20'{1}'&limit=9999".format(host,deployment)
request = rw.getUrl(url,headers)

print json.dumps(request)

r = request['content'][0]

resource_id = r['id']

tenantLabel=r['organization']['tenantLabel']
tenantRef=r['organization']['tenantRef']
subtenantLabel=r['organization']['subtenantLabel']
subtenantRef=r['organization']['subtenantRef']

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

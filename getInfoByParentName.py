#!/usr/bin/env python
import operator
import os
import sys
import json
import time
import pprint

import json

import rw

deployment = sys.argv[1]

host="vra-01a.corp.local"
username="jason@corp.local"
tenant="vsphere.local"
password="VMware1!"

pp = pprint.PrettyPrinter(indent=4)

values = { 'username':username, 'password':password, 'tenant':tenant }
data = json.dumps(values)
headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8'}

r=rw.postUrl("https://{0}/identity/api/tokens".format(host),data=data,headers=headers)

resp = r.json()

id = resp["id"]

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

#url = "https://{0}/catalog-service/api/consumer/resources?$filter=requestNumber%20eq%20{1}".format(host,request_number)
url = "https://{0}/catalog-service/api/consumer/resources?$filter=name%20eq%20'{1}'".format(host,deployment)
request = rw.getUrl(url,headers)


request_id = request['content'][0]['requestId']

url="https://{0}/catalog-service/api/consumer/requests/{1}/resourceViews".format(host,request_id)
request = rw.getUrl(url,headers)

#pp.pprint(request["content"])

for item in request['content']:
	print "Name "+item['name'],item["resourceType"]
	if (item['resourceType'] == "Infrastructure.Virtual"):
		rw.showProperties(item['data'])



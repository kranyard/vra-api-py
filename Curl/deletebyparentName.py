#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json

import rw

deployment = sys.argv[1]

host="vra-01a.corp.local"
username="jason@corp.local"
tenant="vsphere.local"
password="VMware1!"

values = { 'username':username, 'password':password, 'tenant':tenant }
data = json.dumps(values)
headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8'}

req = urllib2.Request("https://{0}/identity/api/tokens".format(host),data=data,headers=headers)

try:
	req = urllib2.urlopen(req,context=context)
except urllib2.HTTPError as e:
	print e.code
	print e.read()


resp=json.loads(req.read())

id = resp["id"]

def getUrl(url,headers):
	req = urllib2.Request(url,headers=headers)

	try:
		req = urllib2.urlopen(req,context=context)
	except urllib2.HTTPError as e:
		print e.code
		print e.read()

	request=json.loads(req.read())
	return [request]

def postUrl(url,headers,data):
	req = urllib2.Request(url,headers=headers,data=data)

	try:
		req = urllib2.urlopen(req,context=context)
	except urllib2.HTTPError as e:
		print e.code
		print e.read()

	request=json.loads(req.read())
	return [request]


headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

#url = "https://{0}/catalog-service/api/consumer/resources?$filter=requestNumber%20eq%20{1}".format(host,request_number)
url = "https://{0}/catalog-service/api/consumer/resources?$filter=name%20eq%20'{1}'".format(host,deployment)

request = getUrl(url,headers)

#print json.dumps(request)

request_id = request[0]['content'][0]['requestId']

cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"  https://{1}/catalog-service/api/consumer/requests/{2}/resourceViews 2> /dev/null".format(id,host,request_id)

stream = os.popen(cmd)

request = json.loads(stream.read())

#print json.dumps(request) 

for c in request["content"]:
	if c["hasChildren"]:
		print "PARENT",c["resourceId"], c["name"]
		resource_id = c["resourceId"]
	else:
		print "CHILD",c["resourceId"], c["name"]

cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"  https://{1}/catalog-service/api/consumer/resources/{2} 2> /dev/null".format(id,host,resource_id)

stream = os.popen(cmd)

item = json.loads(stream.read())

print "RESOURCE",item['id'],item['name']

tenantLabel=item['organization']['tenantLabel']
tenantRef=item['organization']['tenantRef']
subtenantLabel=item['organization']['subtenantLabel']
subtenantRef=item['organization']['subtenantRef']

cmd="curl --insecure -H \"Accept: application/json;charset=UTF-8\" -H \"Content-Type: application/json;charset=UTF-8\" -H \"Authorization: Bearer {0} \"  https://{1}/catalog-service/api/consumer/resources/{2}/actions 2> /dev/null".format(id,host,resource_id)

stream = os.popen(cmd)

request = json.loads(stream.read())

for c in request['content']:
	if c['name'] == "Destroy" : 
		resourceActionRef=c['id']

delete_json={"@type":"ResourceActionRequest","resourceRef":{"id":resource_id }, "resourceActionRef":{"id":resourceActionRef}, "organization":{"tenantRef":tenantRef,"tenantLabel":tenantLabel,"subtenantRef":subtenantRef,"subtenantLabel":subtenantLabel },"state":"SUBMITTED", "requestNumber":0, "requestData":{"entries":[]}}

cmd="curl --verbose --insecure -X POST -H \"Accept: application/json;charset=UTF-8\" -H \"Content-Type: application/json;charset=UTF-8\" -H \"Authorization: Bearer {0} \"  --data \'{2}\' https://{1}/catalog-service/api/consumer/requests 2> /dev/null".format(id,host,json.dumps(delete_json))

stream = os.popen(cmd)


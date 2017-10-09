#!/usr/bin/env python
import json
import operator
import os
import sys
import json
import urllib
import urllib2
import time
import ssl

#buildId = sys.argv[1]

# This restores the same behavior as before.
context = ssl._create_unverified_context()

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

catalogItemName = "library/httpd"

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

# Get catalog item by name, need the catalogItemId
url = "https://{0}/catalog-service/api/consumer/entitledCatalogItemViews?$filter=name%20eq%20%27{1}%27".format(host,catalogItemName)
request = getUrl(url,headers)
select_id=request[0]['content'][0]['catalogItemId']

# Get request template for catalog item
cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"  https://{1}/catalog-service/api/consumer/entitledCatalogItems/{2}/requests/template 2> /dev/null".format(id,host,select_id)
stream = os.popen(cmd)
request = json.loads(stream.read())

#print json.dumps(request) 

# Need to get component name string. This is likely to break, but can't think of a better way yet.
# The name of the component is one of the keys.
# The delete the superfluous data structures to fix template

#print request['data'].keys()

cName=(request['data'].keys())[1]

del request['data'][cName]['data']['networks']
del request['data'][cName]['data']['links']
del request['data'][cName]['data']['log_config']
del request['data'][cName]['data']['health_config']

print json.dumps(request) 
exit(1)

#request['data'][cName]['data']['volumes'][0] = "/root/CS-Demo-{0}/CS-Demo:/usr/local/apache2/htdocs".format(buildId)
#request['data'][cName]['data']['ports'][0]['data']['host_port'] = "80{0}".format(buildId)

# Submit (POST) request using (modified) template 
cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"  --data \'{2}\'  https://{1}/catalog-service/api/consumer/entitledCatalogItems/{3}/requests 2> /dev/null".format(id,host,json.dumps(request),select_id)
stream = os.popen(cmd)
request = json.loads(stream.read())
#print request

# Extract request ID from response
request_id = request['id']
print request_id

cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"  https://{1}/catalog-service/api/consumer/requests/{2} 2> /dev/null".format(id,host,request_id)

while True:
	stream = os.popen(cmd)
	x = json.loads(stream.read())
	print x['requestNumber'],x['id'],x['state'],x['phase']
	time.sleep(10) 
	if x['phase'] == "SUCCESSFUL" : 
		break

cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"  https://{1}/catalog-service/api/consumer/requests/{2}/resourceViews 2> /dev/null".format(id,host,request_id)

stream = os.popen(cmd)

request = json.loads(stream.read())

print json.dumps(request) 

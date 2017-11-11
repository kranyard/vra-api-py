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
import rw

buildId = sys.argv[1]

# Define hostname and credentials
host="vra-01a.corp.local"
username="jason@corp.local"
tenant="vsphere.local"
password="VMware1!"

values = { 'username':username, 'password':password, 'tenant':tenant }
data = json.dumps(values)
headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8'}

r=rw.postUrl("https://{0}/identity/api/tokens".format(host),data=data,headers=headers)

resp = r.json()

print json.dumps(resp)

print "Login token for "+username+" - expires at "+resp["expires"]

id = resp["id"]

catalogItemName = "library/httpd"

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

# Get catalog item by name, need the catalogItemId
url = "https://{0}/catalog-service/api/consumer/entitledCatalogItemViews?$filter=name%20eq%20%27{1}%27".format(host,catalogItemName)
request = rw.getUrl(url,headers=headers)
select_id=request['content'][0]['catalogItemId']

# Get request template for catalog item
url="https://{0}/catalog-service/api/consumer/entitledCatalogItems/{1}/requests/template".format(host,select_id)
request = rw.getUrl(url,headers=headers)

# Need to get component name string. This is likely to break, but can't think of a better way yet.
# The name of the component is one of the keys.
# The delete the superfluous data structures to fix template

cName=request['data'].keys()[1]

del request['data'][cName]['data']['networks']
#del request['data'][cName]['data']['links']
#del request['data'][cName]['data']['log_config']
del request['data'][cName]['data']['health_config']

request['data'][cName]['data']['volumes'][0] = "/root/CS-Demo-{0}/CS-Demo:/usr/local/apache2/htdocs".format(buildId)
request['data'][cName]['data']['ports'][0]['data']['host_port'] = "80{0}".format(buildId)

# Submit (POST) request using (modified) template 
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
print request['content'][0]['name']

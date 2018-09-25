#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import rw

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

blueprint = sys.argv[1]

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url="https://{0}/catalog-service/api/consumer/entitledCatalogItemViews".format(host)
request = rw.getUrl(url,headers)

i=0
for item in request['content']:
	i+=1
	if ( item['name'] == blueprint ):
		select_id=request['content'][i-1]['catalogItemId']

url="https://{0}/catalog-service/api/consumer/entitledCatalogItems/{1}/requests/template".format(host,select_id)
request = rw.getUrl(url,headers)

#print json.dumps(request['data'])
#print request['data']['vSphere__vCenter__Machine_1']['data']['_cluster']
#request['data']['vSphere__vCenter__Machine_1']['data']['_cluster'] = 2
#print request['data']['_number_of_instances']
request['data']['_number_of_instances'] = 10
print "Modified number of instances/deployments : ",request['data']['_number_of_instances']

url="https://{0}/catalog-service/api/consumer/entitledCatalogItems/{1}/requests".format(host,select_id)
r=rw.postUrl(url,headers=headers,data=json.dumps(request))

print r

request = r.json()

request_id = request['id']

url="https://{0}/catalog-service/api/consumer/requests/{1}".format(host,request_id)

while True:
	x = rw.getUrl(url,headers,showUrl=False)
	print x['requestNumber'],x['id'],x['state'],x['phase']
	time.sleep(10) 
	if x['phase'] == "SUCCESSFUL" : 
		break

url="https://{0}/catalog-service/api/consumer/requests/{1}/resourceViews".format(host,request_id)

request = rw.getUrl(url,headers)
print json.dumps(request) 

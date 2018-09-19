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

headers = "-H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"".format(id)

url = "https://{0}/catalog-service/api/consumer/entitledCatalogItemViews".format(host)
request = rw.getUrl(url, headers, showUrl=True) 

i=0
for item in request['content']:
	i+=1
	if ( item['name'] == blueprint ):
		select_id=request['content'][i-1]['catalogItemId']

url = "https://{0}/catalog-service/api/consumer/entitledCatalogItems/{1}/requests/template".format(host,select_id)
request = rw.getUrl(url, headers, showUrl=True) 

#print json.dumps(request) 

print request['data']
#print request['data']['CentOS_6.3']['data']['_cluster']
#request['data']['CentOS_6.3']['data']['_cluster'] = 5
#print request['data']['_number_of_instances']
#request['data']['_number_of_instances'] = 5

data = "\'{0}\'".format(json.dumps(request))
url = "https://{0}/catalog-service/api/consumer/entitledCatalogItems/{1}/requests".format(host,select_id)

request = rw.postUrl(url, headers, data, showUrl=True) 

request_id = request['id']

url = "https://{0}/catalog-service/api/consumer/requests/{1}".format(host,request_id)

while True:
	x = rw.getUrl(url, headers, showUrl=True) 
	print x['requestNumber'],x['id'],x['state'],x['phase']
	time.sleep(10) 
	if x['phase'] == "SUCCESSFUL" : 
		break

url = "https://{0}/catalog-service/api/consumer/requests/{1}/resourceViews".format(host,request_id)
request = rw.getUrl(url, headers, showUrl=True) 

print json.dumps(request) 

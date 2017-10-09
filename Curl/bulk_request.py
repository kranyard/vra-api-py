#!/usr/bin/env python
import operator
import os
import sys
import json
import time

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

blueprint = sys.argv[1]

cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"  https://{1}/catalog-service/api/consumer/entitledCatalogItemViews 2> /dev/null".format(id,host)

stream = os.popen(cmd)

request = json.loads(stream.read())

i=0
for item in request['content']:
	i+=1
	if ( item['name'] == blueprint ):
		select_id=request['content'][i-1]['catalogItemId']

cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"  https://{1}/catalog-service/api/consumer/entitledCatalogItems/{2}/requests/template 2> /dev/null".format(id,host,select_id)

stream = os.popen(cmd)

request = json.loads(stream.read())

#print json.dumps(request) 

print request['data']
#print request['data']['CentOS_6.3']['data']['_cluster']
#request['data']['CentOS_6.3']['data']['_cluster'] = 5
#print request['data']['_number_of_instances']
#request['data']['_number_of_instances'] = 5
exit(1)


cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"  --data \'{2}\'  https://{1}/catalog-service/api/consumer/entitledCatalogItems/{3}/requests 2> /dev/null".format(id,host,json.dumps(request),select_id)

stream = os.popen(cmd)

request = json.loads(stream.read())

request_id = request['id']

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

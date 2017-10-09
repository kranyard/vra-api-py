#!/usr/bin/env python
import operator
import os
import sys
import json
import time
import rw

import json

catalogItemName=raw_input("Enter catalog item : ")
#catalogItemName = sys.argv[1]
#catalogItemName = "CentOS66"

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url="https://{0}/reservation-service/api/reservations/policies".format(host)
request = rw.getUrl(url,headers)

i=0
for item in request['content']:
	i+=1
	print i,"Reservation POLICY",item['id'],item['name']

select=input("Enter reservation policy number ")
res_id = request['content'][select-1]['id']

# Get catalog item by name, need the catalogItemId
url = "https://{0}/catalog-service/api/consumer/entitledCatalogItemViews?$filter=name%20eq%20%27{1}%27".format(host,catalogItemName)
request = rw.getUrl(url,headers)
select_id=request['content'][0]['catalogItemId']

# Get request template for catalog item
url="https://{0}/catalog-service/api/consumer/entitledCatalogItems/{1}/requests/template".format(host,select_id)
request = rw.getUrl(url,headers)

request["data"]["vSphere__vCenter__Machine_1"]["data"]["ReservationPolicyID"] = res_id
print request["data"]["vSphere__vCenter__Machine_1"]["data"]["memory"] 

#print json.dumps(request)
#exit(1)

# Submit (POST) request using (modified) template 
url="https://{0}/catalog-service/api/consumer/entitledCatalogItems/{1}/requests".format(host,select_id)

r = rw.postUrl(url,headers=headers,data=json.dumps(request))

#print r.status_code
#print r.headers

r=rw.getUrl(r.headers['Location'],headers=headers)

print r

# Extract request ID from response
#request_id = request['id']
#print request_id

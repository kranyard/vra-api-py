#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json
import pprint

import urllib

sys.path.append("../")
import rw

pageSize=20

bgName = sys.argv[1]
reservation = sys.argv[2]
storagePath = sys.argv[3]
state = sys.argv[4]

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']
tenant = os.environ['VRATENANT']

debug = True

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

# Get subTenantId (Business Group ID) from name
url="https://{0}/identity/api/tenants/{1}/subtenants?$filter=name eq '{2}'".format(host, tenant, bgName)

request = rw.getUrl(url,headers,showUrl=False)

for c in request["content"]:
    #print "Business group ID "+c["id"]
    bgId = c["id"]


#url = "https://{0}/reservation-service/api/reservations?$filter=substringof('QA',name)".format(host)

url = "https://{0}/reservation-service/api/reservations?limit={1}&$filter=subTenantId eq '{2}' and name eq '{3}'".format(host, pageSize, bgId, reservation)

request = rw.getUrl(url,headers,showUrl=False)

id = request["content"][0]["id"]

url = "https://{0}/reservation-service/api/reservations/{1}".format(host, id)

request = rw.getUrl(url,headers,showUrl=False)

#print (json.dumps(request))
#'.extensionData.entries[] | select(.key == "reservationStorages") .value.items[].values.entries[] | select( .key == "storagePath") .value.label'

found=""

for e in request["extensionData"]["entries"]:

    if e["key"] == "reservationStorages":

        for re in e["value"]["items"]:

            for se in re["values"]["entries"]:

                if se["key"] == "storagePath" and se["value"]["label"] == storagePath:
                    found = re["values"]["entries"]

            for se in found:

                if se["key"] == "storageEnabled":

                    se["value"]["value"] = state

if found == "":
    print ("Storage Path {} not found".format(storagePath))
    exit(1)

request = rw.putUrl(url,headers,showUrl=False,data=json.dumps(request))
print (request)

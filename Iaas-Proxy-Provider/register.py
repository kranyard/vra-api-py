#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json

import rw

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/iaas-proxy-provider/api/machines/register".format(host)

register_json = {  
   #"machineProperties": [  \
   #  { \
   #    "name": "string", \
   #    "virtualMachineId": "string", \
   #    "isRuntime": False, \
   #    "value": "string", \
   #    "isEncrypted": False, \
   #    "isHidden": False, \
   #    "id": "string" \
   #  } \
   #], \
   "virtualMachineId":"4471b58b-7e63-4556-8271-2697c961ff2a", \
   "requestingUser":"jason@corp.local", \
   "deploymentName":"New-Deploy-", \
   "hostReservationId":"e7404501-1598-4263-9f1c-5ddf3cb10e57", \
   "compositeBlueprintId":"Test1", \
   "templateId":"dd3076bc-27f9-4308-a917-896506322462", \
   "owner":"jason@corp.local", \
   "componentId":"MachineA", \
   "hostStorageReservationId":"d35fa878-5063-4099-9b3b-8fddf2ad6a83" \
 }

print json.dumps(register_json)

request = rw.postUrl(url,headers, data=json.dumps(register_json))

print request


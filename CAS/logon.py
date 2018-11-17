#!/usr/bin/env python
import operator
import os
import sys
import json
import getpass

sys.path.append("../")
import rw

refreshToken = sys.argv[1]

authPayload = { 'refreshToken': refreshToken }
data = json.dumps(authPayload)
headers = {'Accept':'application/json','Content-Type':'application/json'}

r=rw.postUrl("https://api.mgmt.cloud.vmware.com/iaas/login",data=data,headers=headers,showUrl=True)

resp = r.json()

print resp["token"]

if "errors" in resp:
	print json.dumps(resp)
	exit(1)

os.environ['CAS_BEARER'] = resp["token"]
os.system("/bin/bash -i") 

#!/usr/bin/env python
import operator
import os
import sys
import json
import rw

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

os.environ['VRATOKEN'] = resp["id"]
os.environ['VRAHOST'] = host
os.system("/bin/bash -i") 

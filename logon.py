#!/usr/bin/env python
import operator
import os
import sys
import json
import getpass
import rw


if ( len(sys.argv) < 2 ):
	print ("logon.py <host> <username> <tenant>")
	exit(1)

# Define hostname and credentials

if ( len(sys.argv) > 1 ):
	host=sys.argv[1]
else:
	host="vra-01a.corp.local"

if ( len(sys.argv) > 2 ):
	username=sys.argv[2]
else:
	username="jason@corp.local"

if ( len(sys.argv) > 3 ):
	tenant = sys.argv[3]
else:
	tenant="vsphere.local"

if ( len(sys.argv) > 4 ):
	password=getpass.getpass()
else:
	password="VMware1!"

values = { 'username':username, 'password':password, 'tenant':tenant }
data = json.dumps(values)
headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8'}

r=rw.postUrl("https://{0}/identity/api/tokens".format(host),data=data,headers=headers,showUrl=False)

resp = r.json()

#print json.dumps(resp)

print "New shell - logged in as "+username+" at "+host+" - expires at "+resp["expires"]

os.environ['VRATOKEN'] = resp["id"]
os.environ['VRATENANT'] = tenant
os.environ['VRAHOST'] = host
os.system("/bin/bash -i") 

#!/usr/bin/env python
import operator
import os
import sys
import json
import getpass
import rw

# Define hostname and credentials

if ( len(sys.argv) > 1 ):
	if ( sys.argv[1] == "help" ):
		print ("logon.py <username> <host> <tenant>")
		exit(1)
	else:
		username=sys.argv[1]
else:
	username="jason@corp.local"

if ( len(sys.argv) > 2 ):
	host=sys.argv[2]
else:
	host="vra-01a.corp.local"

if ( len(sys.argv) > 3 ):
	tenant = sys.argv[3]
else:
	tenant="vsphere.local"

if ( len(sys.argv) > 4 ):
	if ( sys.argv[4] == "prompt" ):
		password=getpass.getpass()
	else:
		password = sys.argv[4]
else:
	password="VMware1!"

print username, host, tenant

values = { 'username':username, 'password':password, 'tenant':tenant }
data = json.dumps(values)
headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8'}

r=rw.postUrl("https://{0}/identity/api/tokens".format(host),data=data,headers=headers,showUrl=True)

resp = r.json()

if "errors" in resp:
	print json.dumps(resp)
	exit(1)

print "Session started as ["+username+"] at ["+host+"] and tenant ["+tenant+"]"
print "Expires at : "+resp["expires"]
print "ID Token : ", resp["id"]

os.environ['VRATOKEN'] = resp["id"]
os.environ['VRATENANT'] = tenant
os.environ['VRAHOST'] = host
os.environ['VRAUSER'] = username
os.environ['VRAEXPIRY'] = resp["expires"]
os.system("/bin/bash -i") 

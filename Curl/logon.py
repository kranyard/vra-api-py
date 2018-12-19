#!/usr/bin/env python
import operator
import os
import sys
import json
import getpass

import rw

if ( len(sys.argv) > 1 ):
	username=sys.argv[1]
else:
	username="jason@corp.local"

if ( len(sys.argv) >= 2 ):
	host=sys.argv[2]
else:
	host="vra-01a.corp.local"

if ( len(sys.argv) >= 3 ):
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

if ( (len(sys.argv) > 1) and (sys.argv[1] == "help") ):
	print ("logon.py <username> <host> <tenant>")
	exit(1)

print username, host, tenant

headers = "-H \"Accept: application/json\" -H \"Content-Type: application/json\""
data = "\'{{\"username\":\"{0}\",\"password\":\"{1}\",\"tenant\":\"{2}\"}}\'".format(username,password,tenant)

url="https://{0}/identity/api/tokens".format(host)

resp = rw.postUrl(url, headers, data, showUrl=True)
#print json.dumps(resp)

print "Session started as ["+username+"] at ["+host+"] and tenant ["+tenant+"]"
print "Expires at : "+resp["expires"]
print "ID Token : ", resp["id"]

os.environ['VRATOKEN'] = resp["id"]
os.environ['VRATENANT'] = tenant
os.environ['VRAHOST'] = host
os.environ['VRAUSER'] = username
os.environ['VRAEXPIRY'] = resp["expires"]
os.system("/bin/bash -i") 

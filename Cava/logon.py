#!/usr/bin/env python
import operator
import os
import sys
import json
import getpass
import requests

requests.packages.urllib3.disable_warnings()

showUrl = True

def getUrl(url,headers,showUrl=showUrl):
	if (showUrl):
		print "GET: "+url
	req = requests.get(url,headers=headers,verify=False)
	return req.json()

def postUrl(url,headers,data,showUrl=showUrl):
	if (showUrl):
		print "POST: "+url
		print data
	r = requests.post(url,headers=headers,data=data,verify=False)
	return(r)

	#print r.status_code
	#print r.headers

	#if ( r.status_code == 200 ):
	#	return r.json()
	


# Define hostname and credentials
host="us08-1-vralb.oc.vmware.com"
username="kranyard@vmware.com"
tenant="cava"
password=getpass.getpass()

values = { 'username':username, 'password':password, 'tenant':tenant }
data = json.dumps(values)
headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8'}

r=postUrl("https://{0}/identity/api/tokens".format(host),data=data,headers=headers,showUrl=False)

resp = r.json()

print json.dumps(resp)

print "Login token for "+username+" - expires at "+resp["expires"]

os.environ['VRATOKEN'] = resp["id"]
os.environ['VRATENANT'] = tenant
os.environ['VRAHOST'] = host
os.system("/bin/bash -i") 

#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json
import pprint
import requests

import rw

newuser = sys.argv[1]

print "Adding "+newuser

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

pp = pprint.PrettyPrinter(indent=4)

debug = False

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/identity/api/tenants/vsphere.local/groups/onboard@vsphere.local".format(host)
request = rw.getUrl(url,headers)
#print json.dumps(request)

update = {}
update['parentGroup'] = request

url = "https://{0}/identity/api/tenants/vsphere.local/principals/?parentGroup=onboard@vsphere.local&page=1&limit=2147483647".format(host)
request = rw.getUrl(url,headers)

print json.dumps(request['content'])

update['users'] = request['content']

url = "https://{0}/identity/api/tenants/vsphere.local/principals/?criteria={1}&limit=12".format(host,newuser)
request = rw.getUrl(url,headers)
#print json.dumps(request)

update['users'].append(request['content'][0])

print json.dumps(update)

url = "https://{0}/identity/api/tenants/vsphere.local/groups/onboard@vsphere.local".format(host)

request = rw.postUrl( url, data=json.dumps(update), headers=headers)
print request.text


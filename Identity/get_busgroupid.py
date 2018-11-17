#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import rw
import urllib

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']
tenant = os.environ['VRATENANT']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

busgroup = sys.argv[1]

# Get subtenantRef
url="https://{0}/identity/api/tenants/{1}/subtenants?$filter=id eq '{2}'".format(host,tenant,busgroup)
url="https://{0}/identity/api/tenants/{1}/subtenants?$filter=name eq '{2}'".format(host,tenant,busgroup)
request = rw.getUrl(url,headers)

print request["content"][0]["id"]
print request["content"][0]["name"]

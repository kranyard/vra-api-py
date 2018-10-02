#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json
import pprint

sys.path.append("../")
import rw

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']
tenant = os.environ['VRATENANT']

pp = pprint.PrettyPrinter(indent=4)

debug = False

bgName = sys.argv[1]

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url="https://{0}/identity/api/tenants/{1}/subtenants?$filter=name eq '{2}'".format(host, tenant, bgName)

#pp.pprint(request["content"])

request = rw.getUrl(url,headers)

for c in request["content"]:
	print c["name"], c["id"]


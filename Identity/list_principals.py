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

pageSize=10000

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']
tenant = os.environ['VRATENANT']

pp = pprint.PrettyPrinter(indent=4)

debug = False

userid = sys.argv[1]

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url="https://{0}/identity/api/tenants/{1}/subtenants/{2}/principals?limit={3}".format(host, tenant, userid, pageSize)

#pp.pprint(request["content"])

flag=True
while flag:

    request = rw.getUrl(url,headers)
    print request
    print request['metadata']
    print request['links']

    url=False
    for l in request["links"]:
        if l["rel"] == "next":
            url = l["href"]
    if (not url):
        flag = False

    for c in request["content"]:
        print c["name"], c["id"]


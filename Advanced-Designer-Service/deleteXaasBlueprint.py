#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json

sys.path.append("../")
import rw

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']
tenant = os.environ['VRATENANT']

bpid = sys.argv[1]

debug = False

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/advanced-designer-service/api/tenants/{1}/blueprints/{2}".format(host, tenant, bpid)
request = rw.deleteUrl(url,headers)


print request["metadata"]
print request

if ( debug ):
	print json.dumps(request)
	exit (0)

#!/usr/bin/env python
import operator
import os
import sys
import json

import rw

bearer = os.environ['CAS_BEARER']

headers = {'Accept':'application/json','Content-Type':'application/json', 'Authorization':"Bearer {0}".format(bearer)}

url = 'https://api.mgmt.cloud.vmware.com/blueprint/api/blueprints'

res = rw.getUrl(url, headers, showUrl=False)

print json.dumps(res)
exit(1)

for r in res['links']:

	url = 'https://api.mgmt.cloud.vmware.com'+r
	bp = rw.getUrl(url, headers, showUrl=False)

	print bp["name"], "[", bp["id"], "]"

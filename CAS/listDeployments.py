#!/usr/bin/env python
import operator
import os
import sys
import json

sys.path.append("../")
import rw

bearer = os.environ['CAS_BEARER']

headers = {'Accept':'application/json','Content-Type':'application/json', 'Authorization':"Bearer {0}".format(bearer)}

url = 'https://api.mgmt.cloud.vmware.com/deployment/api/deployments'

res = rw.getUrl(url, headers)

#print json.dumps(res)

for r in res["results"]:
	print r['name'], r['createdBy'], r["id"]


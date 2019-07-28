#!/usr/bin/env python
import operator
import os
import sys
import json

import rw

bearer = os.environ['CAS_BEARER']

headers = {'Accept':'application/json','Content-Type':'application/json', 'Authorization':"Bearer {0}".format(bearer)}

url = 'https://www.mgmt.cloud.vmware.com/iaas/api/machines/122cafe248ed4797?apiVersion=2019-01-15'

res = rw.deleteUrl(url, headers, showUrl=False)

print (res)
exit(1)

for r in res["content"]:
	print r['name'], r["id"]


#!/usr/bin/env python
import operator
import os
import sys
import json

showUrl = False

#id = sys.argv[1]

import rw

bearer = os.environ['CAS_BEARER']

headers = {'Accept':'application/json','Content-Type':'application/json', 'Authorization':"Bearer {0}".format(bearer)}

url = 'https://api.mgmt.cloud.vmware.com/iaas/api/zones'.format(id)

res = rw.getUrl(url, headers, showUrl=showUrl)

print json.dumps(res)
exit(1)

for i in res["content"]:
	print i["id"], i["externalRegionId"]

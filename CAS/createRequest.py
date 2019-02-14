#!/usr/bin/env python
import operator
import os
import sys
import json


projectId = sys.argv[1]
blueprintId = sys.argv[2]

sys.path.append("../")
import rw

bearer = os.environ['CAS_BEARER']

headers = {'Accept':'application/json','Content-Type':'application/json', 'Authorization':"Bearer {0}".format(bearer)}

request = {
"deploymentName": "Example API",
"projectId": projectId,
"reason": "Create a deployment via API",
"inputs": {},
"blueprintId": blueprintId,
}

url = 'https://api.mgmt.cloud.vmware.com/blueprint/api/blueprint-requests'

res = rw.postUrl(url, headers, data=json.dumps(request))

print res


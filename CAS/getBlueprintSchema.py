#!/usr/bin/env python
import operator
import os
import sys
import json

sys.path.append("../")
import rw

id = sys.argv[1]

bearer = os.environ['CAS_BEARER']

headers = {'Accept':'application/json','Content-Type':'application/json', 'Authorization':"Bearer {0}".format(bearer)}

url = 'https://api.mgmt.cloud.vmware.com/blueprint/api/blueprints/{0}/inputs-schema'.format(id)

res = rw.getUrl(url, headers, showUrl=False)

print json.dumps(res)


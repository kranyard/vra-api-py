#!/usr/bin/env python
import operator
import os
import sys
import json

showUrl = False

sys.path.append("../")
import rw

bearer = os.environ['CAS_BEARER']

headers = {'Accept':'application/json','Content-Type':'application/json', 'Authorization':"Bearer {0}".format(bearer)}

url = 'https://api.mgmt.cloud.vmware.com/iaas/projects'

res = rw.getUrl(url, headers, showUrl=showUrl)

print json.dumps(res)

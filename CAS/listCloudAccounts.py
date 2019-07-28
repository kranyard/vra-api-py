#!/usr/bin/env python
import operator
import os
import sys
import json

import rw

bearer = os.environ['CAS_BEARER']

headers = {'Accept':'application/json','Content-Type':'application/json', 'Authorization':"Bearer {0}".format(bearer)}

url = 'https://api.mgmt.cloud.vmware.com/iaas/api/cloud-accounts-vsphere'

res = rw.getUrl(url, headers, showUrl=False)

print json.dumps(res)


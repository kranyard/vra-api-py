#!/usr/bin/env python
import operator
import os
import sys
import json

showUrl = False

import rw

id = sys.argv[1]

bearer = os.environ['CAS_BEARER']

headers = {'Accept':'application/json','Content-Type':'application/json', 'Authorization':"Bearer {0}".format(bearer)}

#url = 'https://api.mgmt.cloud.vmware.com/iaas/networks?$filter=id+eq+{0}'.format(id)
url = 'https://api.mgmt.cloud.vmware.com/iaas/networks?$filter=externalRegionId+eq+{0}'.format(id)

res = rw.getUrl(url, headers, showUrl=showUrl)

print json.dumps(res)

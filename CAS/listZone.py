#!/usr/bin/env python
import operator
import os
import sys
import json

showUrl = True

id = sys.argv[1]

import rw

bearer = os.environ['CAS_BEARER']

headers = {'Accept':'application/json','Content-Type':'application/json', 'Authorization':"Bearer {0}".format(bearer)}

#url = 'https://api.mgmt.cloud.vmware.com/iaas/api/zones?$filter=externalRegionId+eq+{0}'.format(id)
url = 'https://api.mgmt.cloud.vmware.com/iaas/api/zones?$filter=regionId+eq+\'{0}\''.format(id)
#url = 'https://api.mgmt.cloud.vmware.com/iaas/api/zones'.format(id)

res = rw.getUrl(url, headers, showUrl=showUrl)

print json.dumps(res)

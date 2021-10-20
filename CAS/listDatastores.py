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

url = "https://api.mgmt.cloud.vmware.com/iaas/api/fabric-vsphere-datastores"

url = "https://api.mgmt.cloud.vmware.com/iaas/api/fabric-vsphere-datastores?$filter=cloudAccountIds.item eq '641e2a6f67cf0e75592986c8f387d'"

url = "https://api.mgmt.cloud.vmware.com/iaas/api/fabric-vsphere-datastores?$filter=externalRegionId eq 'Datacenter:datacenter-21'"

res = rw.getUrl(url, headers, showUrl=showUrl)

print json.dumps(res)
exit(1)


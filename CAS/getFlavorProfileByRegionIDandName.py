#!/usr/bin/env python
import operator
import os
import sys
import json

showUrl = True

id = sys.argv[1]
name = sys.argv[2]

import rw

bearer = os.environ['CAS_BEARER']

headers = {'Accept':'application/json','Content-Type':'application/json', 'Authorization':"Bearer {0}".format(bearer)}

url = 'https://api.mgmt.cloud.vmware.com/iaas/api/flavor-profiles?$filter=regionId+eq+{0}'.format(id)

res = rw.getUrl(url, headers, showUrl=showUrl)

print "Profile ID ", res["content"][0]["id"]

mapping = res["content"][0]["flavorMappings"]["mapping"][name]

print "cpuCount : ", mapping["cpuCount"]
print "memoryInMB : ", mapping["memoryInMB"]



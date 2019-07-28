#!/usr/bin/env python
import operator
import os
import sys
import json
import urllib

import rw

refreshToken = sys.argv[1]

casUrl = "api.staging.symphony-dev.com"
casUrl = "api.mgmt.cloud.vmware.com"

authPayload = '{ "refreshToken": '+refreshToken+' }'
data = json.dumps(authPayload)

resp=rw.postUrl("https://{0}/iaas/login".format(casUrl),data=data,showUrl=True)

print resp["token"]

if "errors" in resp:
	print json.dumps(resp)
	exit(1)

os.environ['CAS_BEARER'] = resp["token"]
os.environ['CAS_URL'] = casUrl
os.system("/bin/bash -i") 

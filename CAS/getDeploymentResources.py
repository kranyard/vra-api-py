#!/usr/bin/env python
import operator
import os
import sys
import json

sys.path.append("../")
import rw

deploymentId = sys.argv[1]

bearer = os.environ['CAS_BEARER']

headers = {'Accept':'application/json','Content-Type':'application/json', 'Authorization':"Bearer {0}".format(bearer)}

url = 'https://api.mgmt.cloud.vmware.com/deployment/api/deployments/{0}/resources'.format(deploymentId)

res = rw.getUrl(url, headers, showUrl=False)

print json.dumps(res)	

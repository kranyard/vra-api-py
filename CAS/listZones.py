#!/usr/bin/env python
import operator
import os
import sys
import json

import argparse
import rw

def get_args():
    parser = argparse.ArgumentParser(
        description='List Cloud Zones')

    parser.add_argument('-u', '--showUrl',
                        action='store_true',
                        help="Show REST URL",
                        default=False)

    parser.add_argument('-d', '--debug',
                        action='store_true',
                        help="Debug, just output JSON",
                        default=False)

    args = parser.parse_args()

    return args


args = get_args()

bearer = os.environ['CAS_BEARER']
headers = {'Accept':'application/json','Content-Type':'application/json', 'Authorization':"Bearer {0}".format(bearer)}

url = 'https://api.mgmt.cloud.vmware.com/iaas/api/zones'.format(id)
res = rw.getUrl(url, headers, showUrl=args.showUrl)

if ( args.debug ):
	print json.dumps(res)
	exit(1)

for i in res["content"]:
	print "Zone : ",i["id"], i["name"]

	url = "https://api.mgmt.cloud.vmware.com"+i["_links"]["region"]["href"]
	res = rw.getUrl(url, headers, showUrl=args.showUrl)

	print "Region : ",res["id"], res["externalRegionId"]

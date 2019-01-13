#!/usr/bin/env python
import operator
import os
import sys
import json
import getpass

import argparse

import rw

def get_args():
    parser = argparse.ArgumentParser(
        description='Display vRA resources/items')

    parser.add_argument('-s', '--host',
                        required=False,
                        action='store',
                        help='Hostname of vRA server',
			default = "vra-01a.corp.local")

    parser.add_argument('-u', '--username',
                        required=False,
                        action='store',
                        help='User name',
			default = "jason@corp.local")

    parser.add_argument('-p', '--password',
                        required=False,
                        action='store',
                        help='Password',
			default = "VMware1!")

    parser.add_argument('-t', '--tenant',
                        required=False,
                        action='store',
                        help='Tenant',
			default = "vsphere.local")

    parser.add_argument('-d', '--debug',
                        action='store_true',
                        help="Debug, just output JSON",
                        default=False)

    parser.add_argument('-m', '--metadata',
                        action='store_true',
                        help="Display REST metadata",
                        default=False)

    args = parser.parse_args()

    return args


def main():

	args = get_args() 

	# Define hostname and credentials

	print args.username, args.host, args.tenant

	values = { 'username':args.username, 'password':args.password, 'tenant':args.tenant }
	data = json.dumps(values)
	headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8'}

	r=rw.postUrl("https://{0}/identity/api/tokens".format(args.host),data=data,headers=headers,showUrl=True)

	resp = r.json()

	if "errors" in resp:
		print json.dumps(resp)
		exit(1)

	print "Session started as ["+args.username+"] at ["+args.host+"] and tenant ["+args.tenant+"]"
	print "Expires at : "+resp["expires"]
	print "ID Token : ", resp["id"]

	os.environ['VRATOKEN'] = resp["id"]
	os.environ['VRATENANT'] = args.tenant
	os.environ['VRAHOST'] = args.host
	os.environ['VRAUSER'] = args.username
	os.environ['VRAEXPIRY'] = resp["expires"]
	os.system("/bin/bash -i") 

# Start program
if __name__ == "__main__":
    main()

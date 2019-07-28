#!/usr/bin/env python
import operator
import os
import sys
import json

import rw

import argparse
import getpass
import urllib

def get_args():
    parser = argparse.ArgumentParser(
        description='Find a vRealize Orchestrator workflow by name')

    parser.add_argument('-s', '--host',
                        required=True,
                        action='store',
                        help='vRealize Orchestrator host to connect to')

    parser.add_argument('-o', '--port',
			type=int,
                        action='store',
                        help="optional port to use, default 8281",
                        default=8281)

    parser.add_argument('-u', '--user',
                        required=True,
                        action='store',
                        help='User name to use when connecting to host')

    parser.add_argument('-p', '--password',
                        required=False,
                        action='store',
                        help='Password to use when connecting to host')

    parser.add_argument('-i', '--id',
                        required=True,
                        action='store',
                        help='Name of vRO workflow')

    parser.add_argument('-d', '--debug',
                        action='store_true',
                        help="Debug, just output JSON",
                        default=False)

    parser.add_argument('-x', '--showUrl',
                        action='store_true',
                        help="Show REST URL",
                        default=False)

    args = parser.parse_args()
    if args.password is None:
        args.password = getpass.getpass(
            prompt='Enter password for host %s and user %s: ' %
                   (args.host, args.user))

    return args

args = get_args()

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8' }

url = 'https://' + args.host + ':' + str(args.port) + \
        '/vco/api/workflows/' + args.id

request = rw.getUrl(url,headers, auth=(args.user, args.password), showUrl=args.showUrl)

content = request.json()

if (args.debug):
    print json.dumps(content)
    sys.exit(1)

#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json

import argparse

import rw

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

def get_args():
    parser = argparse.ArgumentParser(
        description='Display vRA resources/items')

    parser.add_argument('-o', '--owner',
                        required=False,
                        action='store',
                        help='Filter resources by owner')

    parser.add_argument('-n', '--name',
                        required=False,
                        action='store',
                        help='Filter resources by substring of machinename')

    parser.add_argument('-p', '--pageSize',
                        type=int,
                        required=False,
                        action='store',
                        default=20,
                        help='REST page size')

    parser.add_argument('-u', '--showUrl',
                        action='store_true',
                        help="Show REST URL",
                        default=False)

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

    headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

    if args.owner is not None:
        url = "https://{0}/catalog-service/api/consumer/resourceViews?$filter=owners/ref+eq+'{1}'&limit={2}".format(host, args.owner, args.pageSize)

    elif args.name is not None:
        url = "https://{0}/catalog-service/api/consumer/resourceViews?$filter=substringof('{1}', name)&limit={2}".format(host, args.name, args.pageSize)
        #url = "https://{0}/catalog-service/api/consumer/resourceViews?$filter=substringof('{1}', name)&withExtendedData=true&withOperations=true&limit={2}".format(host, name, args.pageSize)

    else:
        url = "https://{0}/catalog-service/api/consumer/resources?limit={1}".format(host, args.pageSize)
    

    while url:

        request = rw.getUrl(url,headers, showUrl=args.showUrl)

        if args.debug:
            print json.dumps(request)
        else:
            for c in request["content"]:
                print c["name"],c["status"]

        if args.metadata:
            print "METADATA: "+str(request["metadata"])

        url=False
        for l in request["links"]:
            if l["rel"] == "next":
                url = l["href"]

# Start program
if __name__ == "__main__":
    main()

#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json
import pprint

import argparse

sys.path.append("../")
import rw

def getargs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name',
                        required=False,
                        action='store',
                        help='catalog item by name')
    parser.add_argument('-d', '--setdebug',
                        required=False,
                        action='store_true',
                        help='debug')
    parser.add_argument('-u', '--showurl',
                        required=False,
                        action='store_true',
                        help='showurl')
    args = parser.parse_args()
    return args



def main():
    args = getargs()
    catalogName = args.name
    setdebug = args.setdebug
    showUrl = args.showurl

    if setdebug:
        debug = True
    else:
	debug = False


    host = os.environ['VRAHOST']
    id = os.environ['VRATOKEN']
    headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

    url = "https://{0}//catalog-service/api/catalogItems?$filter=name eq '{1}'".format(host,catalogName)
    request = rw.getUrl(url,headers, showUrl=showUrl)

    print request["content"][0]["name"]

    if debug:
	    print json.dumps(request)

if __name__ == '__main__':
	main()




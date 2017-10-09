#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import urllib

import json
import pprint

import rw

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

tenant = "vsphere.local"
tenant = "Cava"

pp = pprint.PrettyPrinter(indent=4)

debug = False

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/identity/api/tenants/{1}/groups/?groupType=CUSTOM&limit=9999".format(host,tenant)
request = rw.getUrl(url,headers)
for item in request['content']:
	print item['name']

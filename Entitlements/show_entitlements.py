#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json
import pprint

import rw

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

pp = pprint.PrettyPrinter(indent=4)

debug = False

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/entitlements/e47e0416-acc0-4669-b73d-88ea98456efe".format(host)

request = rw.getUrl(url,headers)

#pp.pprint(request)
print json.dumps(request)


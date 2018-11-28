#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import base64

import json

import rw

catId = sys.argv[1]

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

debug = False

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/catalogItems{1}".format(host,catId)
request = rw.getUrl(url,headers)

print request

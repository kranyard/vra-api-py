#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import base64

import json

import rw

iconId = sys.argv[1]

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

debug = False

headers = "-H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"".format(id)
#headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/icons/{1}".format(host, iconId)
request = rw.deleteUrl(url,headers)

print request

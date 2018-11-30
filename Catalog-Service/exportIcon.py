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

url = "https://{0}/catalog-service/api/consumer/entitledCatalogItemViews/{1}".format(host,catId)
request = rw.getUrl(url,headers)

print request['name'], request['iconId']
iconId = request['iconId']

url = "https://{0}/catalog-service/api/icons/{1}?limit=500".format(host, iconId)
request = rw.getUrl(url,headers)

print request["fileName"], request["contentType"]

data = base64.b64decode(request["image"])

imageFile = open(request["fileName"], "wb")

imageFile.write(data)

imageFile.close()

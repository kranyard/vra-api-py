#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json

import rw

deploymentId = sys.argv[1]
name = sys.argv[2]

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

debug = True
showUrl = False

headers = "-H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"".format(id)

url = "https://{0}/catalog-service/api/consumer/deployments/{1}".format(host, deploymentId)
request = rw.getUrl(url,headers, showUrl=showUrl)

print request["name"]

request["name"] = name
request["description"] = "Some text"

print request["expenseMonthToDate"]


request = rw.putUrl(url,headers, showUrl=showUrl, data=json.dumps(request))

print request

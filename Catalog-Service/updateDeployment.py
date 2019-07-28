#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json

import rw

deploymentId = sys.argv[1]

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

debug = True
showUrl = False

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/consumer/deployments/{1}".format(host, deploymentId)
request = rw.getUrl(url,headers, showUrl=showUrl)

print request["name"]

print request["expenseMonthToDate"]

request["expenseMonthToDate"]["amount"] = 16.927799999999998
request["expenseMonthToDate"]["currencyCode"] = "USD"
request["expenseMonthToDate"]["asOnDate"] =  "2019-03-25T02:27:35.421Z"

print request["expenseMonthToDate"]

request = rw.putUrl(url,headers, showUrl=showUrl, data=json.dumps(request))

print request

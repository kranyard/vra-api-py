#!/usr/bin/env python
import operator
import os
import sys
import json

import rw

requestNumber = sys.argv[1]

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url="https://{0}/catalog-service/api/consumer/requests?$filter=requestNumber+eq+{1}".format(host, requestNumber)

request = rw.getUrl(url,headers, showUrl=False)

print json.dumps(request)

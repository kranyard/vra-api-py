#!/usr/bin/env python
import operator
import os
import sys
import json

import rw

requestId = sys.argv[1]

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url="https://{0}/catalog-service/api/consumer/requests/{1}".format(host, requestId)
request = rw.getUrl(url,headers)

print json.dumps(request)
#rw.showProperties(x)


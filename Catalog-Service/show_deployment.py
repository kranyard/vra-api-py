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

if ( debug ):
	print json.dumps(request)
	exit (0)



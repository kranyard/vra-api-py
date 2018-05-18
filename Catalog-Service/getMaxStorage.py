#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json
import pprint

sys.path.append("../")
import rw

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

pp = pprint.PrettyPrinter(indent=4)

debug = False

catId = sys.argv[1]

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/consumer/entitledCatalogItems/{1}/requests/schema".format(host,catId)
request = rw.getUrl(url,headers)

for f in request["fields"]:

	if "classId" in f["dataType"]:
		if f["dataType"]["classId"] == "Blueprint.Component.Declaration":
			print f["label"]
			for g in f["dataType"]["schema"]["fields"]:
				if g['id'] == "storage":
					print "Max Storage : "+str(g['state']['facets'][0]['value']['value']['value'])+"Gb"

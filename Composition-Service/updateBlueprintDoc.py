#!/usr/bin/env python
import operator
import os
import sys
import json

sys.path.append("../")
import rw

debug = False

docid = sys.argv[1]

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/composition-service/api/blueprintdocuments/{1}".format(host, docid)
request = rw.getUrl(url,headers,showUrl=False)

if ( debug ):
	print json.dumps(request)
	exit (0)

#rw.showProperties(request)

for key, value in request.items():
	if ( key == "components" ):
		for k, v in request["components"].items():
			if (request["components"][k]["type"] == "Infrastructure.CatalogItem.Machine.Virtual.vSphere"):
				for i, j in request["components"][k]["data"].items():
					if ( isinstance(j, dict) ):
						if 'visible' in j.keys():
							print i, j
	elif ( key == "properties"):
		for k, v in request[key].items():
			print k, v
		
	elif ( key == "propertyGroups"):
		print "Property Groups"
		for v in request[key]:
			print v
		

request["properties"]["_archiveDays"] = 20
request["properties"]["_leaseDays"] = {"default":1,"max":40,"min":1}

print(request["properties"]["_leaseDays"]["max"])

#request["properties"]["_leaseDays"]["max"] = 50
#del request["properties"]["_leaseDays"]
#del request["properties"]["_archiveDays"]

request = rw.putUrl(url,headers,showUrl=False,data=json.dumps(request))
print request


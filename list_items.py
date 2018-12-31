#!/usr/bin/env python
import operator
import os
import sys
import json

import rw

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

#url = "https://{0}/catalog-service/api/consumer/resources?limit=99999".format(host)
url = "https://{0}/catalog-service/api/consumer/resources/types/composition.resource.type.deployment?%24filter%3D%2528parentResource%2520eq%2520null%2529%2520or%2520%2528parentResource%252Fstatus%2520eq%2520%2527DELETED%2527%2529%2529".format(host)

r = rw.getUrl(url,headers)

print r["metadata"]

parents = r["content"]

for x in parents:
	if x['parentResourceRef'] is None:
		print "PARENT ID",x['id'],x['name']
		url = "https://{0}/catalog-service/api/consumer/resources?%24filter=parentResource+eq+'{1}'".format(host,x['id'])
		z = rw.getUrl(url,headers)

		for c in z["content"]:
			print "CHILD ID",c['id'],c['name']
			#for key, value in c.items():
			#	print key, ':=', value
			#print '-----'
		print '---'


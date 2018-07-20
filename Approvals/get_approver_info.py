#!/usr/bin/env python
import operator
import os
import sys
import json

sys.path.append("../")
import rw

debug = False

name = "Reconfigure001"
pid = "c36a6803-3d82-4e88-b989-c9ef62f1519f"

pageSize=50

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/approval-service/api/policies?limit={1}&$filter=id+eq+'{2}'".format(host, pageSize, pid)

request = rw.getUrl(url,headers)

if ( debug ):
	print json.dumps(request)
	exit (0)

for item in request['content']:
	print "Policy: ["+item['name']+"] ID: ["+item['id']+"]"
	for levels in item['phases'][0]['levels']:
		print "Level : [",levels['name'], "] ID: [", levels['id'], "]"
		for approver in levels['approvers']:
			print "   "+approver['value']

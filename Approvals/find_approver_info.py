#!/usr/bin/env python
import operator
import os
import sys
import json

sys.path.append("../")
import rw

debug = False

level_id = sys.argv[1]

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/approval-service/api/policies".format(host)

request = rw.getUrl(url,headers)

if ( debug ):
	print json.dumps(request)
	exit (0)

for item in request['content']:
	for levels in item['phases'][0]['levels']:
		if ( levels['id'] == level_id ):
			print "Policy: ["+item['name']+"] ID: ["+item['id']+"]"
			print "This level : [",levels['name'], "] ID: [", levels['id'], "] Level Number : [", levels['levelNumber'], "]"
			levelNumber = levels['levelNumber']
			policyId = item['id']

for item in request['content']:
	if ( item['id'] == policyId ):
		for levels in item['phases'][0]['levels']:
			if ( levels['levelNumber'] == levelNumber+1 ) :
				print "Next level : [",levels['name'], "] ID: [", levels['id'], "] Level Number : [", levels['levelNumber'], "]"
				for approver in levels['approvers']:
					print "   "+approver['value']

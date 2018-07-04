#!/usr/bin/env python
import operator
import os
import sys
import json

sys.path.append("../")
import rw

approvalPolicy = sys.argv[1]

debug = False

paging=True
pageSize=50

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/approval-service/api/policies?limit={1}".format(host, pageSize)

flag=True
while flag:

	request = rw.getUrl(url,headers)

	if (paging):
		url=False
		for l in request["links"]:
			if l["rel"] == "next":
				url = l["href"]

		if (not url):
			flag = False
			#print "Complete"
		else:
			print "Next URL "+url
	else:
		flag=False


	if ( debug ):
		print json.dumps(request)
		exit (0)

	for item in request['content']:
		if ( item['name'] == approvalPolicy ):
			print "Policy: ["+item['name']+"] ID: ["+item['id']+"]"
			for levels in item['phases'][0]['levels']:
				print "Level : [",levels['name'], "] ID: [", levels['id'], "]"
				for approver in levels['approvers']:
					print "   "+approver['value']

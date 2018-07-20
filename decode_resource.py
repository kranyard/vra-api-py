#!/usr/bin/env python
import operator
import os
import sys
import json

import rw

machineName = sys.argv[1]

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/catalog-service/api/consumer/resources?$filter=id+eq+'{1}'".format(host, machineName)
data = rw.getUrl(url,headers)

for res in data["content"]:
		
	rw.showProperties(res)


	print "Daily Lease Cost", res['costs']['leaseRate']['cost']['amount']
	print "Cost To Date", res['costToDate']['amount']
	print "Total Cost", res['totalCost']['amount']
	print "Expense month to date", res['expenseMonthToDate']['amount']
	print "  as on", res['expenseMonthToDate']['asOnDate']

	for i in res['resourceData']['entries']:
		print i["key"], i["value"]
		#if (i["value"].contains("value")) :
			#print i["value"]["value"]


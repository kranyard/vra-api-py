#!/usr/bin/env python
import operator
import os
import sys
import json

import rw

import timestring

paging=True
pageSize=5000

filterByDate=False
byYear=2017
ltMon=9
gtMon=6

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url="https://{0}/catalog-service/api/consumer/requests?limit={1}".format(host,pageSize)

users = {}
failed = 0
total = 0
total_catalogItemRequests = 0

months = {}

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
		#else:
			#print "Next URL "+url
	else:
		flag=False

	#print request["metadata"]

	for x in request["content"]:
		ts = timestring.Date(x['dateSubmitted'])
		d = "{0}/{1}/{2}".format(ts.day,ts.month,ts.year)
		m = "{0}/{1}".format(ts.month,ts.year)
		#print "REQUEST",x['id'],x['requestNumber'],x['phase'],x['@type'],x['requestedBy'], x['requestedFor'], x['dateSubmitted'],m
			
		if ( filterByDate ):
			if ( ts.year != byYear ) or ( ts.month > ltMon ) or (ts.month < gtMon ):
				continue ;

		if m in months:
			months[m] += 1
		else:
			months[m] = 1
		
		total += 1

		if ( x['@type'] == 'CatalogItemRequest' ):
			total_catalogItemRequests += 1

			if x['state'] != "SUCCESSFUL":
				failed += 1

			if x['requestedBy'] in users:
				users[x['requestedBy']] += 1
			else:
				users[x['requestedBy']] = 1


# Sort the list and create new list of tuples order by number of requests
sorted_users = sorted(users.items(), key=operator.itemgetter(1))

# Reverse the order (highest first)
sorted_users.reverse() 

if ( filterByDate ):
	print months
	sorted_months = sorted(months.items())
	for i in sorted_months:
		print i[0],i[1]

for i in sorted_users:
	print str(i[0])+","+str(i[1])

print "Total number of users ", len(sorted_users)
print "Total requests: ",total
print "Total Catalog Item Requests: ",total_catalogItemRequests
print "Failed: requests ",failed


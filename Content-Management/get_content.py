#!/usr/bin/env python
import operator
import os
import sys
import json
import time
import urllib
import urllib2
import ssl

import json

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

context = ssl._create_unverified_context()

def getUrl(url,headers):
	req = urllib2.Request(url,headers=headers)

	try:
		req = urllib2.urlopen(req,context=context)
	except urllib2.HTTPError as e:
		print e.code
		print e.read()

	request=json.loads(req.read())
	return [request]

def postUrl(url,headers,data):
	req = urllib2.Request(url,headers=headers,data=data)

	try:
		req = urllib2.urlopen(req,context=context)
	except urllib2.HTTPError as e:
		print e.code
		print e.read()

	request=json.loads(req.read())
	return [request]


headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/content-management-service/api/provider/contenttypes".format(host)
request = getUrl(url,headers)
#print json.dumps(request)

url = "https://{0}/content-management-service/api/contents".format(host)
request = getUrl(url,headers)
print json.dumps(request)



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

contentId = sys.argv[1]

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


	#request=json.loads(req.read())
	#return [request]


headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

# Get catalog item by name, need the catalogItemId
url = "https://{0}/content-management-service/api/contents?$filter=contentId%20eq%20%27{1}%27".format(host,contentId)
request = getUrl(url,headers)

cid = request[0]['content'][0]['id']
print "Content Id: ",cid

dependencies =  request[0]['content'][0]['dependencies']

for d in dependencies:
	print "Dependent content id: ",d

#package_json={"name" : "Demo package", "description" : "Package for demo purposes", "contents" : [ cid, dependencies[0] ]}
package_json={"name" : "Demo package", "description" : "Package for demo purposes", "contents" : [ cid] }
data = json.dumps(package_json)

url="https://{0}/content-management-service/api/packages".format(host)
postUrl(url,headers,data)

request = getUrl(url,headers)
print json.dumps(request)

pid = request[0]['content'][0]['id']
print "Export package :",pid

zipName = contentId

# Export package
cmd="curl --insecure -H \"Accept: application/zip\"  -H \"Authorization: Bearer {0} \" https://{1}/content-management-service/api/packages/{2} -o {3}.zip 2> /dev/null".format(id,host,pid,zipName)
stream = os.popen(cmd)


# Delete package
cmd="curl --insecure -X DELETE -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \" https://{1}/content-management-service/api/packages/{2} 2> /dev/null".format(id,host,pid)
stream = os.popen(cmd)

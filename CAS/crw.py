import operator
import os
import sys
import json

showUrl = True
headers = "-H \"Accept: application/json\" -H \"Content-Type: application/json\""

def getUrl(url,headers,showUrl=showUrl):

	cmd="curl -s -X GET --insecure {0} \"{1}\"".format(headers,url)
	if (showUrl):
		print "GET: "+url
		#print cmd

	stream = os.popen(cmd)

	request = json.loads(stream.read())
	return request

def deleteUrl(url,headers,showUrl=showUrl):
	if (showUrl):
		print "GET: "+url

	cmd="curl -s -X DELETE --insecure {0} \'{1}\'".format(headers,url)
	#print cmd

	stream = os.popen(cmd)

	print stream.read()
	#request = json.loads(stream.read())
	#return request

def postUrl(url,data,showUrl=showUrl):
	if (showUrl):
		print "POST: "+url
		#print data
	cmd="curl -s -X POST --insecure {0} --data {1} \'{2}\'".format(headers,data, url)
	#print cmd

	stream = os.popen(cmd)

	s = stream.read()
	return (json.loads(s))

def putUrl(url,headers,data,showUrl=showUrl):
	if (showUrl):
		print "PUT: "+url
		print data
	cmd="curl -s -X PUT --insecure {0} --data \'{1}\' \'{2}\'".format(headers,data, url)
	#print cmd

	stream = os.popen(cmd)

	print stream.read()
	#request = json.loads(stream.read())
	#return request


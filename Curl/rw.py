import operator
import os
import sys
import json

showUrl = True

def getUrl(url,headers,showUrl=showUrl):
	if (showUrl):
		print "GET: "+url

	cmd="curl -s --insecure {0} \'{1}\'".format(headers,url)

	stream = os.popen(cmd)

	request = json.loads(stream.read())
	return request

def postUrl(url,headers,data,showUrl=showUrl):
	if (showUrl):
		print "POST: "+url
		print data
	cmd="curl -s --insecure {0} --data {1} \'{2}\'".format(headers,data, url)

	stream = os.popen(cmd)

	print stream.read()
	#request = json.loads(stream.read())
	#return request


def findProperties(item, name):
	_findProps(item, name, "", 0)

def _findProps(item, name, k, l):
	p1 = "F"
	p2 = "F"
	for x in range(0,l):
		p1 += "FF"

	for x in range(0,l-1):
		p2 += "FF"

	if isinstance(item, dict):
		print p2+"Dictionary : {"+k+"}"
		for key, value in item.items():
			if (isinstance(value, dict) or isinstance(value, list)):
				_findProps(value, name, str(key),l+1)
			else :
				if ( name == key ):
					print p1+" ["+str(key)+"] ["+str(value)+"]"
	elif isinstance(item, list):
		print p2+"List : {"+k+"}"
		for value in item:	
			if (isinstance(value, dict) or isinstance(value, list)):
				_findProps(value, name, "",l+1)
			else :
				print p1+"L "+str(value)
	else:
		# Scalar
		if ( k != "" ):
			print p1+"SCALAR {"+k+"} "+str(item)
		else:
			print p1+"S "+str(item)

def showProperties(item):
	_showProps(item, "", 0)

def _showProps(item, k, l):
	p1 = ""
	p2 = ""
	for x in range(0,l):
		p1 += "  "

	for x in range(0,l-1):
		p2 += "  "

	if isinstance(item, dict):
		print p2+"Dictionary : {"+k+"}"
		for key, value in item.items():
			if (isinstance(value, dict) or isinstance(value, list)):
				_showProps(value, str(key),l+1)
			else :
				print p1+" ["+str(key)+"] ["+str(value)+"]"
	elif isinstance(item, list):
		print p2+"List : {"+k+"}"
		for value in item:	
			if (isinstance(value, dict) or isinstance(value, list)):
				_showProps(value, "",l+1)
			else :
				print p1+"L "+str(value)
	else:
		# Scalar
		if ( k != "" ):
			print p1+"SCALAR {"+k+"} "+str(item)
		else:
			print p1+"S "+str(item)


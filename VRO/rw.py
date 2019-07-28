import requests

requests.packages.urllib3.disable_warnings()

showUrl = True

def getUrl(url,headers,auth,showUrl=showUrl):
	if (showUrl):
		print "GET: "+url
	r = requests.get(url,headers=headers,auth=auth, verify=False)
	return r

def deleteUrl(url,headers,showUrl=showUrl):
	if (showUrl):
		print "DELETE: "+url
	r = requests.delete(url,headers=headers,verify=False)
	return (r)

def postUrl(url,headers,data,showUrl=showUrl):
	if (showUrl):
		print "POST: "+url
		print data
	r = requests.post(url,headers=headers,data=data,verify=False)
	return(r)

	#print r.status_code
	#print r.headers

	#if ( r.status_code == 200 ):
		#return r.json()


def putUrl(url,headers,data,showUrl=showUrl):
	if (showUrl):
		print "POST: "+url
		print data
	r = requests.put(url,headers=headers,data=data,verify=False)
	return(r)

	#print r.status_code
	#print r.headers

	#if ( r.status_code == 200 ):
		#return r.json()
	

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


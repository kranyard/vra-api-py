import requests

requests.packages.urllib3.disable_warnings()

showUrl = True

def getUrl(url,headers,showUrl=showUrl):
	if (showUrl):
		print "GET: "+url
	req = requests.get(url,headers=headers,verify=False)
	print req
	return req.json()

def postUrl(url,headers,data,showUrl=showUrl):
	if (showUrl):
		print "POST: "+url
		print data
	r = requests.post(url,headers=headers,data=data,verify=False)
	return(r)

	#print r.status_code
	#print r.headers

	#if ( r.status_code == 200 ):
	#	return r.json()
	

def showProperties(item):
	for key, value in item.items():
		if isinstance(value, dict):
			print "DICTIONARY [", key, ']'
			showProperties(value)
		elif isinstance(value, list):
			print "LIST: [", key, ']'
			for v in value:	
				print v
		else:
			# Scalar
			print "[",key, ']:=[', value,']'
	print '-----'


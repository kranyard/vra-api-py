import requests

requests.packages.urllib3.disable_warnings()

showUrl = False

def getUrl(url,headers,showUrl=showUrl):
	if (showUrl):
		print "GET: "+url
	req = requests.get(url,headers=headers,verify=False)
	return req.json()

def postUrl(url,headers,data):
	if (showUrl):
		print "POST: "+url
		print data
	r = requests.post(url,headers=headers,data=data,verify=False)
	return(r)

	#print r.status_code
	#print r.headers

	#if ( r.status_code == 200 ):
	#	return r.json()
	


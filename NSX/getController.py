#!/usr/bin/env python
import operator
import os
import sys
import json

import requests

requests.packages.urllib3.disable_warnings()

showUrl = True

def getUrl(url,headers,showUrl=showUrl):
        if (showUrl):
                print "GET: "+url
        req = requests.get(url,headers=headers,verify=False, auth=('admin','VMware1!'))
	print req.text
        return req.json()

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


host = "nsxmgr-01a.corp.local"

headers = {'Accept':'application/xml','Content-Type':'application/xml'}

url="https://{0}/api/2.0/vdn/controller".format(host)

request = getUrl(url,headers)

print request


#!/usr/bin/env python
import operator
import os
import sys
import json

sys.path.append("../")
import rw

debug = False

docid = sys.argv[1]

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/composition-service/api/blueprintdocuments/{1}".format(host, docid)
request = rw.getUrl(url,headers,showUrl=False)

if ( debug ):
	print json.dumps(request)
	exit (0)

if "_snapshot_propagation" in request["properties"]:
    print request["properties"]["_snapshot_propagation"]
    # Remove propagation flag
    del request["properties"]["_snapshot_propagation"]
else:
    print "No _snapshot_propagation flag"

post = rw.putUrl(url,headers,showUrl=False,data=json.dumps(request))
print post

# Now add flag back as True
request["properties"]["_snapshot_propagation"] = True
post = rw.putUrl(url,headers,showUrl=False,data=json.dumps(request))
print post

request = rw.getUrl(url,headers,showUrl=False)
print request["properties"]["_snapshot_propagation"]

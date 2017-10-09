#!/usr/bin/env python
import operator
import os
import sys
import json

host="vra-01a.corp.local"
username="jason@corp.local"
tenant="vsphere.local"
password="VMware1!"

cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" --data \'{{\"username\":\"{0}\",\"password\":\"{1}\",\"tenant\":\"{2}\"}}\' https://{3}/identity/api/tokens 2> /dev/null".format(username,password,tenant,host)

stream = os.popen(cmd)

id_json = json.loads(stream.read())

print json.dumps(id_json)

#print id_json["id"]

os.environ['VRATOKEN'] = id_json["id"]

os.system("/bin/bash -i") 

#!/usr/bin/env python
import operator
import os
import sys
import json


# Define hostname and credentials
host="cava-n-80-066.eng.vmware.com"
username="fritz@coke.sqa-horizon.local"
tenant="qe"
password="VMware1!"

# Build curl cmd using credentials etc
cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" --data \'{{\"username\":\"{0}\",\"password\":\"{1}\",\"tenant\":\"{2}\"}}\' https://{3}/identity/api/tokens 2> /dev/null".format(username,password,tenant,host)

# Create pipe to execute curl cmd
stream = os.popen(cmd)

# Read JSON payload as response from vRA
id_json = json.loads(stream.read())

# Pretty print of JSON
print json.dumps(id_json)

#print id_json["id"]

# Set OS environment vars
os.environ['VRATOKEN'] = id_json["id"]
os.environ['VRAHOST'] = host

# Spawn new instance shell
os.system("/bin/bash -i") 

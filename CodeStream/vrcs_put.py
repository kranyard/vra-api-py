#!/usr/bin/env python
import operator
import os
import sys
import json

host="vra-01a.corp.local"

id = os.environ['VRATOKEN']

cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \" https://{1}/release-management-service/api/release-pipelines?action=import\&overwrite=false --data @AutoPromote.json 2> /dev/null".format(id,host)

stream = os.popen(cmd)

request = json.loads(stream.read())

print json.dumps(request)

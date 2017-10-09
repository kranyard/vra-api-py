#!/usr/bin/env python
import operator
import os
import sys
import json

host="vra-01a.corp.local"

pipeline = sys.argv[1]

id = os.environ['VRATOKEN']

cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \" https://{1}/release-management-service/api/release-pipelines/{2}/?action=export 2> /dev/null".format(id,host,pipeline)

stream = os.popen(cmd)

request = json.loads(stream.read())

print json.dumps(request)

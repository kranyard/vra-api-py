#!/usr/bin/env python
import operator
import os
import sys
import json

debug = False

pid = sys.argv[1]

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

cmd="curl --insecure -H \"Accept: application/zip\"  -H \"Authorization: Bearer {0} \" https://{1}/content-management-service/api/packages/{2} -o package.zip 2> /dev/null".format(id,host,pid)

stream = os.popen(cmd)

request = json.loads(stream.read())

print json.dumps(request)

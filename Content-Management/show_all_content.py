#!/usr/bin/env python
import operator
import os
import sys
import json

debug = False

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"  https://{1}/content-management-service/api/contents?limit=9999 2> /dev/null".format(id,host)

stream = os.popen(cmd)

request = json.loads(stream.read())

if ( debug ):
        print json.dumps(request)
        exit (0)

for item in request['content']:
        if (item['contentTypeId'] == "composite-blueprint"):
                print "{0} - {1} - [{2}] {3}".format(item['id'],item['contentId'],item['description'],item['contentTypeId'])


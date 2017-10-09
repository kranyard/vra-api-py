#!/usr/bin/env python
import operator
import os
import sys
import json

package_id = sys.argv[1]

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

cmd="curl --insecure -X DELETE -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \" https://{1}/content-management-service/api/packages/{2} 2> /dev/null".format(id,host,package_id)

stream = os.popen(cmd)

request = json.loads(stream.read())

print json.dumps(request)

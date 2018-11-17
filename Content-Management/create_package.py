#!/usr/bin/env python
import operator
import os
import sys
import json

debug = False

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

package_json={"name" : "10ft", "description" : "Package for demo purposes", "contents" : [ "a859833c-2a59-4408-9e8d-7a5c81e730e8","ba22c14c-1cc5-44b0-a4e0-99824a4fc392" ]}
package_json={"name" : "test1", "description" : "Package for demo purposes", "contents" : [ "2792ca64-ac54-4d54-adfe-43df51b97040", "de451a64-f608-4edf-a61a-195d760adcfb" ]}

cmd="curl --insecure -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \" --data \'{2}\' https://{1}/content-management-service/api/packages 2> /dev/null".format(id,host,json.dumps(package_json))

stream = os.popen(cmd)

request = json.loads(stream.read())

print json.dumps(request)

#!/usr/bin/env python
import operator
import os
import sys
import json

debug = False

zipfile = sys.argv[1]

host=os.environ['VRAHOST']
id = os.environ['VRATOKEN']

cmd="curl --insecure -H \"Content-Type: multipart/form-data\"  -H \"Authorization: Bearer {0} \" https://{1}/content-management-service/api/packages -F \"file=@{2}\"".format(id,host,zipfile)

print cmd
stream = os.popen(cmd)

#!/usr/bin/env python
import operator
import os
import sys
import json
import time
import base64
import json

import rw

import pipes

iconId = sys.argv[1]
fileName = sys.argv[2]
contentType = sys.argv[3]

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

debug = False

headers = "-H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"".format(id)
#headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

with open(fileName, "rb") as imageFile:
	 encodedImage = base64.b64encode(imageFile.read())

imageFile.close()

imageBody = {
	"id": iconId,
	"fileName": fileName,
	"contentType": contentType,
	"image" : encodedImage,
	"organization" : {}
}

url = "https://{0}/catalog-service/api/icons".format(host)
request = rw.postUrl(url,headers, data=pipes.quote(json.dumps(imageBody)))

print request

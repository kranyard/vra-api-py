#!/usr/bin/env python
import operator
import os
import sys
import json

component = "native"
out = ""

for line in sys.stdin:
	out += line.rstrip()

payload = json.loads(out)

#componentIdx is set to index in array for selected component
componentIdx=0
for i in payload["fields"]:
        print i["label"]
        if i["label"] == component:
                break
        componentIdx += 1

print componentIdx

maxVolumesIdx=0
for i in payload["fields"][componentIdx]["dataType"]["schema"]["fields"]:
        if i["id"] == "max_volumes":
                break
        maxVolumesIdx += 1

fieldFound=False
maxVolumesDerivedValueIdx=0
for i in payload["fields"][componentIdx]["dataType"]["schema"]["fields"][maxVolumesIdx]["state"]["facets"]:
        if i["type"] == "derivedValue":
                fieldFound=True
                break

        maxVolumesDerivedValueIdx += 1

if (not fieldFound):
        print "No derivedValue field"
        exit(1)

print "Current max_volumes : ",payload["fields"][componentIdx]["dataType"]["schema"]["fields"][maxVolumesIdx]["state"]["facets"][maxVolumesDerivedValueIdx]["value"]["value"]["value"]

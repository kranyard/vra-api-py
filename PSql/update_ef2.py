#!/usr/bin/env python
import operator
import os
import sys
import json

import psycopg2

machineName = sys.argv[1]

conn = psycopg2.connect(host="vra-01a.corp.local",database="vcac", user="vcac", password="nD7KlfAojxotuZl2")

cur = conn.cursor()

sql = "select parentresource_id from cat_resource where name = '{0}'".format(machineName)
print sql

cur.execute(sql)
out = ((cur.fetchone())[0])
cur.close()

resourceId = out

cur = conn.cursor()

sql = "select eff_schema from comp_deployment where cafe_resource_id  = '{0}'".format(resourceId)
print sql

cur.execute(sql)
out = ((cur.fetchone())[0])

payload = json.loads(out)

component = sys.argv[2]
newStorageMaxValue = sys.argv[3]
newMaxVolumesDerivedValue = sys.argv[4]

vals = ""

componentIdx=0
for i in payload["fields"]:
	if i["label"] == component:
		vals = i
		break
#componentIdx is set to index in array for selected component
	componentIdx += 1

props = ""

storageIdx=0
for i in payload["fields"][componentIdx]["dataType"]["schema"]["fields"]:
	if i["id"] == "storage":
		break
	storageIdx += 1


storageMaxValueIdx=0


for i in payload["fields"][componentIdx]["dataType"]["schema"]["fields"][storageIdx]["state"]["facets"]:
	if i["type"] == "maxValue":
		break 
	storageMaxValueIdx += 1

print "Current max storage : ",payload["fields"][componentIdx]["dataType"]["schema"]["fields"][storageIdx]["state"]["facets"][storageMaxValueIdx]["value"]["value"]["value"]
payload["fields"][componentIdx]["dataType"]["schema"]["fields"][storageIdx]["state"]["facets"][storageMaxValueIdx]["value"]["value"]["value"] = newStorageMaxValue

maxVolumesIdx=0
for i in payload["fields"][componentIdx]["dataType"]["schema"]["fields"]:
	if i["id"] == "max_volumes":
		break
	maxVolumesIdx += 1


maxVolumesDerivedValueIdx=0
for i in payload["fields"][componentIdx]["dataType"]["schema"]["fields"][maxVolumesIdx]["state"]["facets"]:
	if i["type"] == "derivedValue":
		break
	maxVolumesDerivedValueIdx += 1

print "Current max_volumes : ",payload["fields"][componentIdx]["dataType"]["schema"]["fields"][maxVolumesIdx]["state"]["facets"][maxVolumesDerivedValueIdx]["value"]["value"]["value"]
payload["fields"][componentIdx]["dataType"]["schema"]["fields"][maxVolumesIdx]["state"]["facets"][maxVolumesDerivedValueIdx]["value"]["value"]["value"] = newMaxVolumesDerivedValue

cur.close()

cur = conn.cursor()
cur.execute("UPDATE comp_deployment SET eff_schema=(%s) WHERE cafe_resource_id = (%s)", (json.dumps(payload),resourceId,));
conn.commit()
cur.close()


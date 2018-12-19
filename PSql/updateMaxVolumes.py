#!/usr/bin/env python
import operator
import os
import sys
import json

import psycopg2

machineName = sys.argv[1]
component = sys.argv[2]
newMaxVolumesDerivedValue = sys.argv[3]

psqlhost = os.environ['PSQLHOST']
psqldb = os.environ['PSQLDB']
psqluser = os.environ['PSQLUSER']
psqlpwd = os.environ['PSQLPWD']

conn = psycopg2.connect(host=psqlhost,database=psqldb, user=psqluser, password=psqlpwd)

cur = conn.cursor()
sql = "select parentresource_id from cat_resource where name = '{0}'".format(machineName)
print sql
cur.execute(sql)
resourceId = ((cur.fetchone())[0])
cur.close()

cur = conn.cursor()
sql = "select eff_schema from comp_deployment where cafe_resource_id  = '{0}'".format(resourceId)
print sql
cur.execute(sql)
out = ((cur.fetchone())[0])
cur.close()
payload = json.loads(out)

#componentIdx is set to index in array for selected component
componentIdx=0
for i in payload["fields"]:
	if i["label"] == component:
		break
	componentIdx += 1

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
payload["fields"][componentIdx]["dataType"]["schema"]["fields"][maxVolumesIdx]["state"]["facets"][maxVolumesDerivedValueIdx]["value"]["value"]["value"] = int(newMaxVolumesDerivedValue)

print "New max_volumes : ",payload["fields"][componentIdx]["dataType"]["schema"]["fields"][maxVolumesIdx]["state"]["facets"][maxVolumesDerivedValueIdx]["value"]["value"]["value"]

cur = conn.cursor()
cur.execute("UPDATE comp_deployment SET eff_schema=(%s) WHERE cafe_resource_id = (%s)", (json.dumps(payload),resourceId,));
conn.commit()
cur.close()

#!/usr/bin/env python
import operator
import os
import sys
import json
import psycopg2

psqlhost = os.environ['PSQLHOST']
psqldb = os.environ['PSQLDB']
psqluser = os.environ['PSQLUSER']
psqlpwd = os.environ['PSQLPWD']

conn = psycopg2.connect(host=psqlhost,database=psqldb, user=psqluser, password=psqlpwd)

machineName = sys.argv[1]
label = sys.argv[2]

cur = conn.cursor()
cur.execute("select parentresource_id from cat_resource where name = '{0}'".format(machineName))
resourceId = ((cur.fetchone())[0])
cur.close()


cur = conn.cursor()
cur.execute("select eff_schema from comp_deployment where cafe_resource_id  = '{0}'".format(resourceId))
out = ((cur.fetchone())[0])
cur.close()

props = json.loads(out)

vals = ""
for i in props["fields"]:
    #print i["label"]
    if i["label"] == label:
		vals = i


if ( vals == "" ):
    print "Label ["+label+"] not found"
    exit(1)

props = ""
for i in vals["dataType"]["schema"]["fields"]:
	#print i["id"]
	if i["id"] == "max_volumes":
		props = i	

print "max_volumes"
for i in props["state"]["facets"]:
	print i["type"], i["value"]["value"]["value"]



#!/usr/bin/env python
import operator
import os
import sys
import json

import pprint

import psycopg2

def showTables(tableName):

	q = """                              
	SELECT column_name, data_type, is_nullable
	FROM information_schema.columns
	WHERE table_name = %s;
	"""

	cur = conn.cursor()
	cur.execute(q, (tableName,))  # (table_name,) passed as tuple
	result = cur.fetchall()

	for i in result:
		print i[0]
	cur.close()


psqlhost = os.environ['PSQLHOST']
psqldb = os.environ['PSQLDB']
psqluser = os.environ['PSQLUSER']
psqlpwd = os.environ['PSQLPWD']

conn = psycopg2.connect(host=psqlhost,database=psqldb, user=psqluser, password=psqlpwd)

machineName = sys.argv[1]

cur = conn.cursor()
cur.execute("select parentresource_id from cat_resource where name = '{0}'".format(machineName))
out = ((cur.fetchone())[0])
cur.close()

resourceId = out

cur = conn.cursor()
cur.execute("select eff_state from comp_deployment where cafe_resource_id  = '{0}'".format(resourceId))
out = ((cur.fetchone())[0])


props = json.loads(out)
print(out)
exit(1)

vals = props["valueMap"]["CentOS_6.3"]["values"]

print "Storage : ", vals["storage"]["value"]["value"]
print "Max Volumes : ", vals["max_volumes"]["value"]["value"]
print "CPU : ", vals["cpu"]["value"]["value"]
print "Memory : ", vals["memory"]["value"]["value"]
if vals["reservation_policy"]["value"] != None:
	print "Reservation Policy : ", vals["reservation_policy"]["value"]["value"]

print

for i in vals.keys():
	if "value" in vals[i].keys():
		if vals[i]["value"] == None:
			print i, "[Has no setting]"
		else:
			if "value" in vals[i]["value"].keys():
				print i, "["+str(vals[i]["value"]["value"])+"]"

cur.close()


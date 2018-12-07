#!/usr/bin/env python
import operator
import os
import sys
import json

import pprint

import psycopg2

def showProperties(item):
        _showProps(item, "", 0)

def _showProps(item, k, l):
        p1 = ""
        p2 = ""
        for x in range(0,l):
                p1 += "  "

        for x in range(0,l-1):
                p2 += "  "

        if isinstance(item, dict):
                print p2+"Dictionary : {"+k+"}"
                for key, value in item.items():
                        if (isinstance(value, dict) or isinstance(value, list)):
                                _showProps(value, str(key),l+1)
                        else :
                                print p1+" ["+str(key)+"] ["+str(value)+"]"
        elif isinstance(item, list):
                print p2+"List : {"+k+"}"
                for value in item:
                        if (isinstance(value, dict) or isinstance(value, list)):
                                _showProps(value, "",l+1)
                        else :
                                print p1+"L "+str(value)
        else:
                # Scalar
                if ( k != "" ):
                        print p1+"SCALAR {"+k+"} "+str(item)
                else:
                        print p1+"S "+str(item)

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


pp = pprint.PrettyPrinter(indent=4)

conn = psycopg2.connect(host="vra-01a.corp.local",database="vcac", user="vcac", password="nD7KlfAojxotuZl2")

machineName = sys.argv[1]

cur = conn.cursor()
cur.execute("select parentresource_id from cat_resource where name = '{0}'".format(machineName))
out = ((cur.fetchone())[0])
cur.close()

resourceId = out

cur = conn.cursor()
cur.execute("select eff_schema from comp_deployment where cafe_resource_id  = '{0}'".format(resourceId))
out = ((cur.fetchone())[0])

p1 = json.loads(out)

#showProperties(props["fields"])

vals = ""

x=0
for i in p1["fields"]:
	print i["label"]
	if i["label"] == "CentOS_6.3":
		print x
		vals = i
	x += 1

props = ""

x=0
for i in vals["dataType"]["schema"]["fields"]:
	#print i["id"]
	if i["id"] == "storage":
		print x
		props = i	
	x += 1

p = ""

print
print "storage"
x=0
for i in props["state"]["facets"]:
	print i["type"], i["value"]["value"]["value"]
	if i["type"] == "maxValue":
		p = i["value"]["value"]["value"]
		print x
	x += 1

print p1["fields"][0]["dataType"]["schema"]["fields"][8]["state"]["facets"][0]["value"]["value"]["value"]
p1["fields"][0]["dataType"]["schema"]["fields"][8]["state"]["facets"][0]["value"]["value"]["value"] = 20

x=0
for i in vals["dataType"]["schema"]["fields"]:
	#print i["id"]
	if i["id"] == "max_volumes":
		props = i	
		print x
	x += 1

print
print "max_volumes"
x=0
for i in props["state"]["facets"]:
	if i["type"] == "derivedValue":
		p = i["value"]["value"]["value"]
		print x
	x += 1

print p1["fields"][0]["dataType"]["schema"]["fields"][37]["state"]["facets"][0]["value"]["value"]["value"]
p1["fields"][0]["dataType"]["schema"]["fields"][37]["state"]["facets"][0]["value"]["value"]["value"] = 2

cur.close()


cur = conn.cursor()
cur.execute("UPDATE comp_deployment SET eff_schema=(%s) WHERE cafe_resource_id = (%s)", (json.dumps(p1),resourceId,));
conn.commit()
cur.close()


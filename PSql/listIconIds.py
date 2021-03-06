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

psqlhost = os.environ['PSQLHOST']
psqldb = os.environ['PSQLDB']
psqluser = os.environ['PSQLUSER']
psqlpwd = os.environ['PSQLPWD']

conn = psycopg2.connect(host=psqlhost,database=psqldb, user=psqluser, password=psqlpwd)

cur = conn.cursor()
cur.execute("select * from cat_icon")
result = cur.fetchall()

for i in result:
	print i[0]
cur.close()

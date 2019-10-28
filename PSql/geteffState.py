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

cur = conn.cursor()
cur.execute("select parentresource_id from cat_resource where name = '{0}' and parentresource_id IS NOT NULL".format(machineName))
resourceId = ((cur.fetchone())[0])
cur.close()

cur = conn.cursor()
cur.execute("select eff_state from comp_deployment where cafe_resource_id  = '{0}'".format(resourceId))
eff_state = ((cur.fetchone())[0])
cur.close()

print eff_state

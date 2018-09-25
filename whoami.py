#!/usr/bin/env python
import operator
import os
import sys
import json
import time

if ( 'VRAHOST' in os.environ ):
	host = os.environ['VRAHOST']
	id = os.environ['VRATOKEN']
	tenant = os.environ['VRATENANT']
	username = os.environ['VRAUSER']
	expiry = os.environ['VRAEXPIRY']
else:
	print "No active session"
	exit(1)


print "Connected to ["+host+"], tenant ["+tenant+"], as user ["+username+"]"
print "Token : "+id
print "Expires : "+expiry

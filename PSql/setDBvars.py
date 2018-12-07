#!/usr/bin/env python
import operator
import os
import sys
import json
import getpass

os.environ['PSQLHOST']=sys.argv[1]
os.environ['PSQLDB']="vcac"
os.environ['PSQLUSER']="vcac"
os.environ['PSQLPWD']=sys.argv[2]

os.system("/bin/bash -i") 

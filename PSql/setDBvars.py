#!/usr/bin/env python
import operator
import os
import sys
import json
import getpass

#os.environ['PSQLHOST']=sys.argv[1]
#os.environ['PSQLDB']="vcac"
#os.environ['PSQLUSER']="vcac"
#os.environ['PSQLPWD']=sys.argv[2]

os.environ['PSQLHOST']="vra-ing-db.csl.vmware.com"
os.environ['PSQLDB']="vcac_ing_prd_march26"
os.environ['PSQLUSER']="postgres"
os.environ['PSQLPWD']=""

os.system("/bin/bash -i") 

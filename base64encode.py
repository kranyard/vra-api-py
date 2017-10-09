#!/usr/bin/env python
import operator
import os
import sys
import json

import getpass

import base64


password = getpass.getpass()

print base64.b64encode(password)

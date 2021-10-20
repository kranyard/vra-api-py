#!/usr/bin/env python
import operator
import os
import sys
import json
import time

import json
import pprint

import urllib

sys.path.append("../")
import rw

pageSize=20

storagePath = sys.argv[1]
newPriority = sys.argv[2]

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']
tenant = os.environ['VRATENANT']

debug = True

headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8', 'Authorization':"Bearer {0}".format(id)}

url = "https://{0}/reservation-service/api/reservations?limit={1}".format(host, pageSize)

flag=True
while flag:

    request = rw.getUrl(url,headers,showUrl=False)

    for i in request["content"]:
        id = i["id"]
        name = i["name"]

        url = "https://{0}/reservation-service/api/reservations/{1}".format(host, id)

        r = rw.getUrl(url,headers,showUrl=False)

        found=""

        for e in r["extensionData"]["entries"]:

            if e["key"] == "reservationStorages":
                for re in e["value"]["items"]:
                    for se in re["values"]["entries"]:
                        if se["key"] == "storagePath" and se["value"]["label"] == storagePath:
                            found = re["values"]["entries"]
                    for se in found:
                        if se["key"] == "storageReservationPriority":
                            print ("Reservation [{}] Storage Path [{}] - Priority [{}] New Priority [{}]".format(name, storagePath, se["value"]["value"], newPriority)) 
                            se["value"]["value"] = newPriority

        if found != "":
            #print (json.dumps(r,indent=4))
            r = rw.putUrl(url,headers,showUrl=False,data=json.dumps(r))
            print (r)

    url=False
    for l in request["links"]:
        if l["rel"] == "next":
            url = l["href"]
    if (not url):
        flag = False


#!/usr/bin/env python
import operator
import os
import sys
import json
import getpass
import argparse
import urllib

showUrl = False

def getUrl(url,headers,showUrl=showUrl):
	
	cmd="curl -s -X GET --insecure {0} \"{1}\"".format(headers,url)
	if (showUrl):
		print "GET: "+url
		#print cmd

	stream = os.popen(cmd)

	request = json.loads(stream.read())
	return request

def deleteUrl(url,headers,showUrl=showUrl):
	if (showUrl):
		print "GET: "+url

	cmd="curl -s -X DELETE --insecure {0} \'{1}\'".format(headers,url)
	#print cmd

	stream = os.popen(cmd)

	print stream.read()
	#request = json.loads(stream.read())
	#return request

def postUrl(url,headers,data,showUrl=showUrl):
	if (showUrl):
		print "POST: "+url
		#print data
	cmd="curl -s -X POST --insecure {0} --data {1} \'{2}\'".format(headers,data, url)
	#print cmd

	stream = os.popen(cmd)

	s = stream.read()
	return (json.loads(s))

def putUrl(url,headers,data,showUrl=showUrl):
	if (showUrl):
		print "PUT: "+url
	print data
	cmd="curl -s -X PUT --insecure {0} --data {1} \'{2}\'".format(headers,data, url)
	#print cmd

	stream = os.popen(cmd)

	print stream.read()
	#request = json.loads(stream.read())
	#return request


def get_args():
    parser = argparse.ArgumentParser(
        description='Display vRA resources/items')

    parser.add_argument('-s', '--host',
                        required=False,
                        action='store',
                        help='Hostname of vRA server',
            default = "vra-01a.corp.local")

    parser.add_argument('-u', '--username',
                        required=False,
                        action='store',
                        help='User name',
            default = "jason@corp.local")

    parser.add_argument('-p', '--password',
                        required=False,
                        action='store',
                        help='Password',
            default = "VMware1!")

    parser.add_argument('-t', '--tenant',
                        required=False,
                        action='store',
                        help='Tenant',
            default = "vsphere.local")

    parser.add_argument('-x', '--prompt',
                        action='store_true',
                        help="Prompt for password",
                        default=False)

    parser.add_argument('-l', '--pageSize',
                        type=int,
                        required=False,
                        action='store',
                        default=20,
                        help='REST page size')

    parser.add_argument('-q', '--showUrl',
                        action='store_true',
                        help="Show REST URL",
                        default=False)

    parser.add_argument('-d', '--debug',
                        action='store_true',
                        help="Debug, just output JSON",
                        default=False)

    parser.add_argument('-m', '--metadata',
                        action='store_true',
                        help="Display REST metadata",
                        default=False)

    args = parser.parse_args()

    if args.prompt:
        args.password = getpass.getpass(
            prompt='Enter password for host %s and user %s: ' %
                   (args.host, args.username))

    return args

def main():

	args = get_args() 

	# Get logon token

	headers = "-H \"Accept: application/json\" -H \"Content-Type: application/json\""
	data = "\'{{\"username\":\"{0}\",\"password\":\"{1}\",\"tenant\":\"{2}\"}}\'".format(args.username,args.password,args.tenant)

	resp=postUrl("https://{0}/identity/api/tokens".format(args.host),data=data,headers=headers,showUrl=args.showUrl)

	#print "Session started as ["+args.username+"] at ["+args.host+"] and tenant ["+args.tenant+"]"
	#print "Expires at : "+resp["expires"]
	#print "ID Token : ", resp["id"]

	id = resp["id"]
	host = args.host

	headers = "-H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"".format(id)

	url = "https://{0}/catalog-service/api/consumer/resources?limit={1}&%24filter=resourceType/name+eq+'Deployment'".format(host, args.pageSize)

	print "Machine, Deployment, ID, Machine ID, Owner, IP address, Memory, BlueprintName, Reservation, State"

	while url:

		request = getUrl(url,headers, showUrl=args.showUrl)

		if args.debug:
			print json.dumps(request)
			sys.exit(0)

		if args.metadata:
			print "METADATA: "+str(request["metadata"])
			print "LINKS: "+str(request["links"])

		for deployment in request["content"]:

			resourceId = deployment["id"]
			requestId = deployment["requestId"]

			# Get request details (for request number)
			#url = "https://{0}/catalog-service/api/consumer/requests/{1}".format(host, requestId)
			#requestNumber = getUrl(url,headers, showUrl=args.showUrl)["requestNumber"]

			# Get all children of this deployment
			url = "https://{0}/catalog-service/api/consumer/resources?limit={1}&%24filter=parentResource/id+eq+'{2}'".format(host, args.pageSize, resourceId)
			crequest = getUrl(url,headers, showUrl=args.showUrl)

			for child in crequest["content"]:
				if child["resourceTypeRef"]["label"] == "Virtual Machine":
					machineId = child["id"]
					ipaddress = ""
					machineStatus = ""
					machineMemory = ""
					machineBlueprintName = ""
					machineReservation = ""

					for res in child["resourceData"]["entries"]: 
						if res["key"] == "ip_address":
							ipAddress = res["value"]["value"]
						if res["key"] == "MachineStatus":
							machineStatus = res["value"]["value"]
						if res["key"] == "MachineMemory":
							machineMemory = res["value"]["value"]
						if res["key"] == "MachineBlueprintName":
							machineBlueprintName = res["value"]["value"]
						if res["key"] == "MachineReservationName":
							machineReservation = res["value"]["value"]

					print ("{0}, \"{1}\", {2}, {3}, {4}, {5}, {6}, \"{7}\", {8}, {9}".format(
						# Machine name
						child["name"], 
						# Deployment name
						deployment["name"],
						# Deployment resource ID
						str(resourceId),
						# Machine resource id
						str(machineId),
						# Owner
						deployment["owners"][0]["ref"],
						# IP address
						ipAddress, 
						# Memory
						machineMemory,
						# Blueprint
						machineBlueprintName,
						# Reservation
						machineReservation,
						# Power status
						machineStatus
						))
				

		url=False
		for l in request["links"]:
			if l["rel"] == "next":
				# Fix url for curl - $ breaks the url
				url = l["href"].replace("$", "%24")
				if args.metadata:
					print "Next URL : ", url

# Start program
if __name__ == "__main__":
	main()

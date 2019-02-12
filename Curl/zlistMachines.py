#!/usr/bin/env python
import operator
import os
import sys
import json

import argparse

sys.path.append("../")
import rw

host = os.environ['VRAHOST']
id = os.environ['VRATOKEN']

def get_args():
    parser = argparse.ArgumentParser(
        description='Display vRA resources/items')

    parser.add_argument('-o', '--owner',
                        required=False,
                        action='store',
                        help='Filter resources by owner')

    parser.add_argument('-p', '--pageSize',
                        type=int,
                        required=False,
                        action='store',
                        default=20,
                        help='REST page size')

    parser.add_argument('-u', '--showUrl',
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

    return args


def main():

	args = get_args() 

	headers = "-H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer {0} \"".format(id)

	if args.owner is not None:
		url = "https://{0}/catalog-service/api/consumer/resources?%24filter=owners/ref+eq+'{1}'+and+resourceType/name+eq+'Deployment'&limit={2}".format(host, args.owner, args.pageSize)

	else:
		url = "https://{0}/catalog-service/api/consumer/resources?limit={1}&%24filter=resourceType/name+eq+'Deployment'".format(host, args.pageSize)

	#url = "https://{0}/catalog-service/api/consumer/resources?%24filter=owners/ref+eq+'{1}'+and+substringof('{2}', name)&limit={3}".format(host, username, machinename, args.pageSize )

	while url:

		request = rw.getUrl(url,headers, showUrl=args.showUrl)

		if args.debug:
			print json.dumps(request)
			sys.exit(0)

		if args.metadata:
			print "METADATA: "+str(request["metadata"])

		for deployment in request["content"]:

			resourceId = deployment["id"]
			requestId = deployment["requestId"]
			# Get request details (for request number)
			url = "https://{0}/catalog-service/api/consumer/requests/{1}".format(host, requestId)
			requestNumber = rw.getUrl(url,headers, showUrl=args.showUrl)["requestNumber"]

			# Get all children of this deployment
			url = "https://{0}/catalog-service/api/consumer/resources?limit={1}&%24filter=parentResource/id+eq+'{2}'".format(host, args.pageSize, resourceId)
			crequest = rw.getUrl(url,headers, showUrl=args.showUrl)

			for child in crequest["content"]:
				if child["resourceTypeRef"]["label"] == "Virtual Machine":
					for res in child["resourceData"]["entries"]: 
						if res["key"] == "ip_address":
							ipAddress = res["value"]["value"]
						if res["key"] == "MachineStatus":
							machineStatus = res["value"]["value"]

					print ("{0}, \"{1}\", {2}, {3}, {4}".format(
						child["name"],
						deployment["name"],
						str(deployment["id"]),
						str(requestNumber),
						deployment["owners"][0]["ref"]))
				

		url=False
		for l in request["links"]:
			if l["rel"] == "next":
				url = l["href"]
				print "URL:",url

# Start program
if __name__ == "__main__":
	main()

#!/usr/bin/env python
import operator
import os
import sys
import json

import rw

import argparse
import getpass
import urllib

import datetime
from time import gmtime, strftime, strptime

def get_args():
    parser = argparse.ArgumentParser(
        description='Display execution time and status of running workflow')

    parser.add_argument('-s', '--host',
                        required=True,
                        action='store',
                        help='vRealize Orchestrator host to connect to')

    parser.add_argument('-o', '--port',
                        type=int,
                        action='store',
                        help="optional port to use, default 8281",
                        default=8281)

    parser.add_argument('-u', '--user',
                        required=True,
                        action='store',
                        help='User name to use when connecting to host')

    parser.add_argument('-p', '--password',
                        required=False,
                        action='store',
                        help='Password to use when connecting to host')

    parser.add_argument('-n', '--name',
                        required=True,
                        action='store',
                        help='Name of vRO workflow')

    parser.add_argument('-d', '--debug',
                        action='store_true',
                        help="Debug, just output JSON",
                        default=False)

    parser.add_argument('-x', '--showUrl',
                        action='store_true',
                        help="Show REST URL",
                        default=False)

    args = parser.parse_args()
    if args.password is None:
        args.password = getpass.getpass(
            prompt='Enter password for host %s and user %s: ' %
                   (args.host, args.user))

    return args

def link_to_dict(link):
    """
    Unmarshal a link object into a Python dictionary
    Returns a Dict
    """

    attributes = link['attributes']

    # Use item.get('value') as value may not be defined for some attributes
    d = dict([(item['name'], item.get('value')) for item in attributes])
    return d


def main():

    args = get_args()

    headers = {'Accept':'application/json;charset=UTF-8','Content-Type':'application/json;charset=UTF-8' }

    """
    url = 'https://' + args.host + ':' + str(args.port) + '/vco/api/workflows/?conditions=name=' + args.name
    """

    url = 'https://{0}:{1}/vco/api/workflows/?conditions=name={2}'.format(args.host, args.port, args.name)

    request = rw.getUrl(url,headers, auth=(args.user, args.password), showUrl=True)

    if request is None:
        print 'HTTP request failed'
        sys.exit(1)


    content = request

    if (args.debug):
        print json.dumps(content)
        sys.exit(1)

    if content['total'] == 0:
        print "Couldn't find workflow named: %s" % args.name
        sys.exit(1)

    # Print workflow info. May be more than one with same name.
    print 'Found %i workflow(s) with name: %s' % (content['total'], args.name)
    # print json.dumps(content['link'])
    links = content['link']
    for link in links:
        workflow = link_to_dict(link)
        # print 'Workflow info for id: %s' % workflow['id']
        workflow = link_to_dict(link)
        # for k, v in workflow.iteritems():
            # print 'X %s : %s' % (k, v)

        workflowId = workflow['id']

        url = 'https://' + args.host + ':' + str(args.port) + \
            '/vco/api/workflows/' + workflowId+"/executions"

        request = rw.getUrl(url,headers, auth=(args.user, args.password), showUrl=args.showUrl)

        if request is None:
            print 'HTTP request failed'
            sys.exit(1)

        content = request

        if (args.debug):
            print json.dumps(content)
            sys.exit(1)

        # Print workflow info. May be more than one with same name.
        relations = content['relations']
        for l in relations["link"]:
            if 'attributes' in l:
                token = link_to_dict(l)
                    
                
            
                now = datetime.datetime.now()

                if ( token["state"] != "completed" ):

                    for k, v in token.iteritems():
                        print '%s : %s' % (k, v)

                    
                    t = datetime.datetime.strptime(token["startDate"], '%Y-%m-%dT%H:%M:%S.%fZ')
                    print ("Running for : " + str(now - t))


# Start program
if __name__ == "__main__":
    main()


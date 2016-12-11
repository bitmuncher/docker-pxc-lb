#!/usr/bin/env python

import os
import sys
from subprocess import call

configfile = '/etc/haproxy/haproxy.cfg'
template = 'server name ip:3306 check port 9200 inter 12000 rise 3 fall 3'

serverlist = os.environ['SERVERS']

if not serverlist:
    print "No servers defined. Exit!"
    sys.exit(100)

servers = serverlist.split(',')
addservers = ''
configdata = ''

i = 1
for server in servers:
    name = 'pxc' + str(i)
    ip = server
    mystr = template;
    mystr = mystr.replace('name', name)
    mystr = mystr.replace('ip', ip)
    addservers = addservers + '    ' + mystr + "\n"
    i = i + 1
    
with open(configfile, 'r') as myfile:
    configdata = myfile.read().replace('{servers}', addservers)
    
f = open(configfile, 'w')
f.write(configdata)

#!/usr/bin/python
#coding:utf8
from saltapi import *
#import saltapi

sapi = saltAPI()
#params = {'client':'local', 'fun':'test.ping', 'tgt':'*'}

#params = {'client':'local','tgt':'*', 'fun':'cmd.run', 'arg1':'hello'}

#params = {'client':'local','tgt':'*', 'fun':'cmd.run', 'arg1':'hostname'}
params = {'client':'local','tgt':'*', 'fun':'cmd.run', 'arg1':'touch /root/cc.txt;touch cc1.txt'}

test = sapi.saltCmd(params)
#test = sapi.saltCmd()
print test


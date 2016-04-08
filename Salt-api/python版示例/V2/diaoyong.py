#!/usr/bin/python
#coding:utf8
from saltapi import *
import saltapi

sapi = saltAPI()
#定义params
params = {'client':'local', 'fun':'test.ping', 'tgt':'*'}
test = sapi.saltCmd(params)
#test = sapi.saltCmd()
print test


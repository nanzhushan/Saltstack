#!/usr/bin/python
# -*- coding: utf-8 -*-
#Modify:knight
#查看python安装了哪些模块可以使用 help('modules')
# 
import pycurl
import StringIO
 
#登录salt-api,获取token
def api_login():
    global token
    url='https://192.168.0.197:8000/login'
    ch=pycurl.Curl()
    ch.setopt(ch.URL, url)
    info = StringIO.StringIO()
    ch.setopt(ch.WRITEFUNCTION, info.write)
    ch.setopt(ch.POST, True)
    #如果是https就要开启这两行
    ch.setopt(ch.SSL_VERIFYPEER, 0)
    ch.setopt(ch.SSL_VERIFYHOST, 2)
    ch.setopt(ch.HTTPHEADER, ['Accept: application/x-yaml'])
    ch.setopt(ch.POSTFIELDS, 'username=saltapi&password=password&eauth=pam')   ##username就是账号 password就是密码
    #要包头信息
    #ch.setopt(ch.HEADER, True)
    #不要包头信息
    ch.setopt(ch.HEADER,False)
    ch.perform()
    html = info.getvalue()
    #提取token
    token = html.split("\n")[-3].replace("\n", '')
    token = token.split(' ')[3]
    info.close()
    ch.close()
 
def api_exec(target, fun, arg='', arg_num=0):
    global token
    url='https://192.168.0.197:8000/'
    ch=pycurl.Curl()
    ch.setopt(ch.URL, url)
    info = StringIO.StringIO()
    ch.setopt(ch.WRITEFUNCTION, info.write)
    ch.setopt(ch.POST, True)
    ch.setopt(ch.SSL_VERIFYPEER, 0)
    ch.setopt(ch.SSL_VERIFYHOST, 2)
    ch.setopt(ch.HTTPHEADER, ['Accept: application/x-yaml', "X-Auth-Token: %s" %(token)])
    if arg_num == 0:
        ch.setopt(ch.POSTFIELDS, "client=local&amp;tgt=%s&amp;fun=%s" %(target, fun))
    elif arg_num == 1:
        ch.setopt(ch.POSTFIELDS, "client=local&amp;tgt=%s&amp;fun=%s&amp;arg=%s" %(target, fun, arg))
    ch.setopt(ch.HEADER,False)
    ch.perform()
    html = info.getvalue()
    info.close()
    ch.close()
    return html
 
#测试时用的,做为模块使用时请注释下面两行,作为模块就是不需要每次都写验证代码。以模块形式导入，调用时候就只要最后两行即可，第一行就是调用登录模块 
api_login()
print api_exec('HD1', 'test.ping', '', 0)


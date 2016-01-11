#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'c8d8z8@gmail.com'

import sys

user = ''
passwd = ''

for arg in sys.argv:
    #print arg
    if arg.startswith('-u'):
        user = arg.replace('-u','',1)
        
    if arg.startswith('-p'):
        passwd = arg.replace('-p','',1)
        
print 'user-'+user
print 'passwd-' + passwd

import commonlib.http
import commonlib.path
url = 'http://10.10.96.143/portal/login.php'
data = 'opr=pwdLogin&userName='+user+'&pwd='+passwd+'&rememberPwd=0'
data = commonlib.http.request(url,commonlib.http.paramparse(data))
print data.decode('utf-8').encode('gbk')
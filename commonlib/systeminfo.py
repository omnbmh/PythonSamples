#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'c8d8z8@gmail.com'


os_id = 'Linux'
os_coding = 'utf-8'

import platform

#Windows will be : (32bit, WindowsPE)
#Linux will be : (32bit, ELF)
print(platform.architecture())

#Windows will be : Windows-XP-5.1.2600-SP3 or Windows-post2008Server-6.1.7600
#Linux will be : Linux-2.6.18-128.el5-i686-with-redhat-5.3-Final
print(platform.platform())

#Windows will be : Windows
#Linux will be : Linux
print(platform.system())
os_id = platform.system()

#Windows and Linux will be : 3.1.1 or 3.1.3
print(platform.python_version())

if os_id == 'Windows':
    os_coding = 'GBK'
    
if os_id == 'Linux':
    os_coding = 'UTF-8'
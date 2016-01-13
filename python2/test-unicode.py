#!/bin/python
# -*- coding:utf-8 -*-
# author c8d8z8@gmail.com

import sys

print sys.getdefaultencoding()

print '中文'.decode('utf-8').encode('gbk')
print u'中文'
print u'中文'.encode('gbk')
print u'中文'.encode('utf-8')
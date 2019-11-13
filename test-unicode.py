#!/bin/python
# -*- coding:utf-8 -*-
# author c8d8z8@gmail.com

import sys

print sys.getdefaultencoding()

print '中文'.decode('utf-8').encode('gbk')
print u'中文'
print u'中文'.encode('gbk')
print u'中文'.encode('utf-8')

# print('\u6c5f\u82cf \u65e0\u952'.decode('unicode-escape').encode('utf-8'))


data = [u'[\u4e50\u989c\u300d\u5c0f\u53ef\u7231', u'\u82b1\u6912\u53f7\uff1a200603919', u'\u5c71\u4e1c \u67a3\u5e84']

for d in data:
    print(d)
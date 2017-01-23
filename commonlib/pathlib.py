#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'c8d8z8@gmail.com'

import sys,os
import systeminfo

print systeminfo.os_id
print systeminfo.os_coding

def cur_dir():
    path = sys.path[0]
    path = unicode(path,systeminfo.os_coding)
    
    print path.encode(systeminfo.os_coding)
    
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)
        
def cur_file_dir(filename):
    return os.path.join(cur_dir(),filename)
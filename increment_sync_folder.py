#!/usr/bin/python
# -*- coding: utf-8 -*-

##########################################
#
# 20160926
# 比对两个目录文件的md5 并生成.md5文件
##########################################
__author__ = 'c8d8z8@gmail.com'

# 配置日志
import commonlib.logginglib
commonlib.logginglib.configure('logging.conf')
logger = commonlib.logginglib.getLogger('zqb')

import hashlib
import os, sys

def calFileMD5(filepath):
    with open(filepath, "rb") as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        print(hash)
        return hash

def gci(path):
    parents = os.listdir(path)
    for parent in parents:
        child = os.path.join(path,parent)
        if os.path.isdir(child):
            gci(child)
            # print(child)
        else:
            print(child)
            fullpath = os.path.abspath(child)
            #createFileMD5(fullpath)


def createFileMD5(dirpath):
    print(dirpath)
    filemd5 = calFileMD5(dirpath)
    file_object = open(dirpath+'.md5', 'w')
    file_object.write(filemd5)
    file_object.close()

if __name__ == "__main__":
    #calFileMD5("test1.txt")
    #calFileMD5("test2.txt")
    gci(".")

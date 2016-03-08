#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'c8d8z8@gmail.com'

import datetime
import random

def dateRandomID():
    '''
    随机产生20位的字符串 前14位是时间 后6位是随机数
    '''
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(0, 999999)).zfill(6)


if __name__ == '__main__':
    for i in range(1,1000):
        print dateRandomID()
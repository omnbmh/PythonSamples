#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
ConfigParser 模块使用

key value 之间可以使用 = : 分隔

'''
import ConfigParser

conf = ConfigParser.ConfigParser()
conf.read('test.conf')

print conf.get('root', 'abc')
print conf.get('emt', 'test')
print conf.get('emt', 'test2')
print conf.get('emt', 'test3')
# 配置文件中 key 和 value = 号前后都可有空格 下面的取法不可取
# print conf.get('emt', 'test3 ')

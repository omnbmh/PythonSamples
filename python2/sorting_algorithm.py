#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- author: c8d8z8@gmail.com

'''
各种排序算法
'''
import random

def createNumArrayList():
    size = 10
    num_array = []
    for i in range(size):
        num_array.append(random.randint(1,100))
    return num_array

#print(createNumArrayList())

def quickSearch(num_array):
    if num_array!=[]:
        base_num = num_array[0]

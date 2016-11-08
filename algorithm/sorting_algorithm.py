#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- author: c8d8z8@gmail.com

'''
各种排序算法
'''
import random

EX_ARRAY = [10,9,4,7,2,1,6,5,3,8];
#EX_ARRAY = [2,6,5,7,4,3,1]

def createNumArrayList():
    size = 10
    num_array = []
    for i in range(size):
        num_array.append(random.randint(1,100))
    return num_array

#print(createNumArrayList())

def bubbleSort(num_array):
    """ 冒泡排序
    Args:
    Returns:
    Raises:
    """
    for i in range(0, len(num_array) - 2, 1):
        for j in range(0, len(num_array) - 1 - i, 1):
            if num_array[j] > num_array[j+1]:
                temp = num_array[j]
                num_array[j] = num_array[j+1]
                num_array[j+1] = temp
                print "exchange num_array[%d]:%d num_array[%d]:%d " % (j, num_array[j], j + 1, num_array[j + 1])
                print num_array

def insertSort(num_array):
    """ 直接插入排序
    Args:
    Returns:
    Raises:
    """
    for i in range(1, len(num_array)):
        if (num_array[i] < num_array[i-1]):
            temp = num_array[i];
            for j in range(i-1, -1, -1):
                if num_array[j] > temp:
                    num_array[j + 1] = num_array[j];
                    num_array[j] = temp
                    print num_array
            #num_array[j+1] = temp;
            print num_array

def quickSort(num_array,start_idx,end_idx):
    """ 快速排序
    Args:
    Returns:
    Raises:
    """
    if num_array!=[] and start_idx < end_idx:
        print "num_array start_idx:%d end_idx:%d" % (start_idx, end_idx)
        base_num = num_array[start_idx]
        l = start_idx
        r = end_idx
        while l < r:
            while l < r and base_num <= num_array[r]:
                r = r - 1
            if l < r:
                num_array[l] = num_array[r]
                num_array[r] = base_num
                print "right-left exchange num_array[%d]:%d num_array[%d]:%d " % (l, num_array[l], r, num_array[r])
                print num_array
                l = l + 1
            while l < r and base_num > num_array[l]:
                l = l + 1
            if l < r:
                num_array[r] = num_array[l]
                num_array[l] = base_num
                print "left-right exchange num_array[%d]:%d num_array[%d]:%d" % (r, num_array[r], l, num_array[l])
                print num_array
                r = r - 1
        quickSort(num_array, start_idx, l-1)
        quickSort(num_array, l+1, end_idx)


if __name__ == "__main__":
    print EX_ARRAY
    #quickSort(EX_ARRAY,0,len(EX_ARRAY)-1)
    #bubbleSort(EX_ARRAY)
    insertSort(EX_ARRAY)
    print EX_ARRAY
    #print range(5,-1,-1)

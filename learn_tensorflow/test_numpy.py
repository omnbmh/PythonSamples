# -*- coding: utf-8 -*-

import numpy as np

a = np.array([1, 2, 5, 4, 3])  # create array

print(a)
print(a[:3])  # first 3
print(a.min())
a.sort()  # 从小到大排序
print(a)

b = np.array([[1, 2, 3], [4, 5, 6]])
print (b * b)

print(np.linspace(1, 100, 10))  # 创建等差数列

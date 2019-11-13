# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x) + 1
z = np.cos(x ** 2) + 1
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

plt.figure(figsize=(8, 4))  # 设置图像大小
plt.plot(x, y, label='$\sin x+1$', color="red", linewidth=2)
plt.plot(x, z, 'b--', label="$\cos x^2+1$")
plt.xlabel('Time(s) ')
plt.ylabel('Volt ')
plt.title('测试 matplot')
plt.ylim(0, 2.2)
plt.legend()
plt.show()


# 生成一个数组格子 用于生成一个 坐标x -3 到 3 y坐标 -2 到 2  的坐标集 间隔 0.5
def anna():
    xx, yy = np.mgrid[-3:3:.1, -2:2:.1]
    print (type(xx))
    print ('-- xx')
    print (xx)
    print ('-- yy')
    print (yy)
    grid = np.c_[xx.ravel(), yy.ravel()]
    print (type(grid))
    print ('-- grid')
    print(grid)
    plt.scatter(grid[:, 0], grid[:, 1])
    plt.show()

if __name__ == '__main__':
    anna()

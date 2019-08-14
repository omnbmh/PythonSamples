# -8- coding:utf-8 -8-

'''
测试正则
'''

import re

FTLE_TYPE_RE = r'.*(.jpg|.png)$'

print(re.match(FTLE_TYPE_RE, "a.jpg", re.I))
print(re.match(FTLE_TYPE_RE, "b.png", re.I))
print(re.match(FTLE_TYPE_RE, "c.pdf", re.I))
print(re.match(FTLE_TYPE_RE, "c.jpga", re.I))

if re.match(r'.*QH1', '_LC_QH1_non_h265_SD_17948245615656747051009629_OX.flv'):
    print('http://qh1.com')
else:
    print('not match')

# 返回是一个数组
print(re.findall('(\w+:\d+)', "花椒直播 -美颜椒友，疯狂卖萌 - 高颜值的直播App"))

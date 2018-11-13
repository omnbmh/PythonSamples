# -8- coding:utf-8 -8-

"""
读取和展示图片
"""
import cv2

TEST_JPG = 'test_image/gdg.jpg'

img = cv2.imread(TEST_JPG, 1)  # 0 灰度图 1 彩色图
cv2.imshow('image window', img)
# 暂停下 为了显示图片
cv2.waitKey(0)

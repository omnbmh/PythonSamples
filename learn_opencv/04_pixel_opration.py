# -8- coding:utf-8 -8-

import cv2

# 550*312
TEST_JPG = 'test_image/gdg.jpg'

img = cv2.imread(TEST_JPG, 1)
# opencv 读取出来的 b g r 颜色值 使用的 元祖

(b, g, r) = img[10, 10]
print(b, g, r)
# 在图片 x 高 10-100 宽 100 的位置 画一条 红色的线
for i in range(1, 100):
    img[10 + i, 100] = (0, 0, 255)

cv2.imshow("image window", img)
cv2.waitKey(0)

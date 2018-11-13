# -8- coding:utf-8 -8-

import cv2

TEST_JPG = 'test_image/gdg.jpg'
img = cv2.imread(TEST_JPG, 1)
cv2.imwrite("test_image/gdg_copy.jpg", img)

# 不同图片质量保存
cv2.imwrite("test_image/gdg_quality_50.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 0])  # 质量 0-100 有损失压缩


# 转换成 PNG 无损 可以设置透明度
cv2.imwrite("test_image/gdg.jpg_compass_50.png", img, [cv2.IMWRITE_PNG_COMPRESSION, 9])

# 对于JPG 数字越小 取值 0-100 压缩比 越高 ，对于PNG 数字越小 取值 0-9 压缩比越低
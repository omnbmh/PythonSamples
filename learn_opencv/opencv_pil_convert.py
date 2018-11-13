# -8- coding:utf-8 -8-

import cv2
from PIL import Image

import numpy as np


def image_cv2_to_pil():
    img = cv2.imread("test_image/yueyunpeng.jpeg")
    cv2.imshow("OpenCV", img)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    image.save("test_image/yunyuepeng_image_cv2_to_pil.jpeg")
    image.show()
    cv2.waitKey()


def image_pil_to_cv2():
    image = Image.open("test_image/yueyunpeng.jpeg")
    print(image.size)  # 图片的尺寸
    print(image.mode)  # 图片的模式
    print(image.format)  # 图片的格式
    image.show()
    img = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)

    cv2.imshow("OpenCV", img)
    cv2.waitKey()


if __name__ == '__main__':
    # image_cv2_to_pil()
    image_pil_to_cv2()

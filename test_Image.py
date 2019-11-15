# -8- coding:utf-8 -8-

'''
Image library (PIL)
Python 图像处理库
'''

from PIL import Image
import numpy as np


def show_image(img_path):
    img = Image.open(img_path)
    img.show()


def print_image_info(img_path):
    img = Image.open(img_path)
    print("--- Image Info ---")
    print(img.format)
    print(img.size)
    print(img.mode)


def resize_image(img_path):
    img = Image.open(img_path)
    print(type(img))  # <class 'PIL.JpegImagePlugin.JpegImageFile'>
    print_image_info(img_path)
    img_resize = img.resize((480, 360), Image.ANTIALIAS)  # 消除锯齿
    # img_arr = np.array(img_resize)
    img_arr = np.array(img_resize.convert('L'))  # 灰度图

    # 从数组保存图片
    new_image = Image.fromarray(img_arr)
    new_image.save("test_image_resize_L.jpeg")


if __name__ == '__main__':
    img_path = 'test_image.jpeg'
    # show_image(img_path)
    resize_image(img_path)

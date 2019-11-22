# -8- coding:utf-8 -8-

'''
Image library (PIL)
Python 图像处理库
'''

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np
import random


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


def generate_captcha(weight, hight, str, bg_color, line_count, point_count):
    # 生成一个Image 指定大小 和 背景色
    image = Image.new('RGB', (weight, hight), bg_color)

    # 来一个画笔
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/msyh.ttf", size=36)

    # 把字写到Image上
    draw.text((12, 0), str, (0, 0, 0), font=font)

    if line_count:
        for i in range(line_count):
            x1 = random.randint(0, weight)
            x2 = random.randint(0, weight)
            y1 = random.randint(0, hight)
            y2 = random.randint(0, hight)
            draw.line((x1, y1, x2, y2), fill=(123, 234, 123))

    if point_count:
        for i in range(point_count):
            x = random.randint(0, weight)
            y = random.randint(0, hight)
            draw.arc((x, y, x + 2, y + 2), 0, 90, fill=(234, 123, 234))
    image.save(str + '.png', 'png')


if __name__ == '__main__':
    img_path = 'test_image.jpeg'
    # show_image(img_path)
    # resize_image(img_path)
    generate_captcha(48, 48, 'A', (255, 255, 255), 0, 0)

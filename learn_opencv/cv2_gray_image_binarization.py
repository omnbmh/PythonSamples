# -8- coding: utf-8 -8-

# 将如图像转为 灰度图 随后二值化 尽量展示轮廓

import cv2

IMG_PATH = 'test_image/648000.jpg'
IMG_PATH_FMT = 'test_image/6480_%s.jpeg'

if __name__ == "__main__":
    image = cv2.imread(IMG_PATH)
    if image is not None:
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(IMG_PATH_FMT % 'gray', image_gray)
        for i in range(5, 255, 5):
            print('thresh is ' + str(i))
            ret, thresh = cv2.threshold(image_gray, i, 255, cv2.THRESH_BINARY)
            cv2.imwrite(IMG_PATH_FMT % ('thresh' + str(i)), thresh)
    else:
        print("read image error!")

# -8- coding: utf-8 -8-

# 尝试使用opencv将卷积过程中的图片展示出来
import cv2
import numpy as np


def max_pooling_forward(z, pooling, strides=(2, 2), padding=(0, 0)):
    """
    最大池化前向过程
    :param z: 卷积层矩阵,形状(N,C,H,W)，N为batch_size，C为通道数
    :param pooling: 池化大小(k1,k2)
    :param strides: 步长
    :param padding: 0填充
    :return:
    """
    N, C, H, W = z.shape
    # 零填充
    padding_z = np.lib.pad(z, ((0, 0), (0, 0), (padding[0], padding[0]), (padding[1], padding[1])), 'constant',
                           constant_values=0)

    # 输出的高度和宽度
    out_h = (H + 2 * padding[0] - pooling[0]) // strides[0] + 1
    out_w = (W + 2 * padding[1] - pooling[1]) // strides[1] + 1

    pool_z = np.zeros((N, C, out_h, out_w))

    for n in np.arange(N):
        for c in np.arange(C):
            for i in np.arange(out_h):
                for j in np.arange(out_w):
                    pool_z[n, c, i, j] = np.max(padding_z[n, c,
                                                strides[0] * i:strides[0] * i + pooling[0],
                                                strides[1] * j:strides[1] * j + pooling[1]])
    return pool_z


if __name__ == '__main__':
    fname = 'test_image/6480.jpg'
    # img = cv2.imread("pic.jpg", cv2.IMREAD_COLOR) 读取一副彩色图片，图片的透明度会被忽略，默认为该值，实际取值为1；
    # img = cv2.imread("pic.jpg", cv2.IMREAD_GRAYSCALE) 以灰度模式读取一张图片，实际取值为0
    # img = cv2.imread("pic.jpg", cv2.IMREAD_UNCHANGED) 加载一副彩色图像，透明度不会被忽略。

    image = cv2.imread(fname)
    # 灰色-COLOR_BGR2GRAY 彩色-COLOR_BGR2RGB
    image_data = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imwrite("test_image/6480.jpg", image_data)
    print('gray image write ok.')

    w4 = np.zeros((4, 3, 2, 1))
    print(w4)
    for i in range(8):
        # filter 生成一个 3*3 的 滤波器
        kernel = np.random.random((3, 3))
        print('--- filter ---')
        print(kernel)
        processed = cv2.filter2D(image_data, -1, kernel)
        print('--- filter2D shape ---')
        print(processed.shape)
        cv2.imwrite("test_image/6480_cnn_" + str(i) + ".jpg", processed)
        print('cnn ' + str(i) + ' image write ok.')
        max_pooled = max_pooling_forward(processed.reshape(-1, 1, 60, 160), (2, 2))
        print('--- max pooling shape ---')
        print(max_pooled.shape)
        cv2.imwrite("test_image/6480_maxpool_" + str(i) + ".jpg", max_pooled[0][0])
        print('max pool ' + str(i) + ' image write ok.')
        print('----- end -----')

# -*- coding:utf-8 -*-

"""
你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
iPhone5 分辨率为(1136,640)
"""


import glob
from PIL import Image


# 得到指定目录下所有图片的列表
def get_imagelist():
    return glob.glob('D:/everyday/record-python/img/*.jpg')


# 图片处理
def image_process(image, num, size=(1136, 640)):
    img = Image.open(image)
    sizex, sizey = img.size
    if sizex > size[0]:
        sizex = size[0]
    if sizey > size[1]:
        sizey = size[1]
    img = img.resize((sizex, sizey))
    num = str(num)
    img.save(num + '.jpg', 'jpeg')


def main():
    image_list = get_imagelist()
    n = 1
    for image in image_list:
        image_process(image, n)
        n += 1


if __name__ == '__main__':
    main()
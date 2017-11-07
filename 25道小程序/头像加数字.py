# -*- coding:utf-8 -*-

from PIL import Image, ImageFont, ImageDraw

import random

"""
在微信图片加上数字
"""


def add_num():
    filepath = 'D:/everyday/record-python/weixin.jpg'
    img = Image.open(filepath)
    x, y = img.size  # 得到头像的宽和高
    print x, y

    draw = ImageDraw.Draw(img)
    text = str(random.randint(1, 99))  # 生成随机数字
    print text

    font = ImageFont.truetype('Arial.ttf', 100)
    draw.text((x - 120, 0), text=text, fill='blue', font=font)  # 修改图像

    img.save('result.jpg', 'jpeg')  # 保存图像


if __name__ == '__main__':
    add_num()
# -*- coding: utf-8 -*-


from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def generator_verification_code():
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype('Arial.ttf', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=(random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)))
    # 输出文字:
    for t in range(4):
        char = chr(random.randint(65, 90))
        text = char
        draw.text((60 * t + 10, 10), text, font=font,
                  fill=(random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)))
    # 模糊:
    image = image.filter(ImageFilter.BLUR)

    # # 存储到内存中
    # tmps = cStringIO.StringIO()
    # image.save(tmps, 'jpeg')
    # res = Response()
    # res.headers.set('Content-Type', 'image/JPEG;charset=utf-8')
    # res.set_data(tmps.getvalue())
    # return res


generator_verification_code()

# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup


def get_image():

    n = 1

    url = 'http://tieba.baidu.com/p/2166231880'

    request = requests.get(url).text

    response = request.encode('utf-8')

    soup = BeautifulSoup(response, 'html.parser')

    img_urls = soup.find_all('img', class_='BDE_Image')
    print img_urls
    for img in img_urls:

        # url = soup.find_all('img', class_='BDE_Image')[0]['src']
        #
        # print url
        text = requests.get(img['src'])

        filepath = 'url/{0}.{1}'.format(n, 'jpg')

        with open(filepath, 'wb') as f:
            f.write(text.content)
        n += 1

        print text


def get_dog():
    n = 1
    for i in range(1, 5):
        url = 'http://www.tuku.cn/bizhi/tuji2715_page{0}.aspx'.format(i)  # format还是挺好的，用好了可以简化代码很多
        res = requests.get(url)
        print(res)
        soup = BeautifulSoup(res.text, 'html.parser')
        img_urls = soup.find_all('div', class_='disp_img1')
        print img_urls
        for img_url in img_urls:
            img_res = requests.get(img_url.find_all('img')[0]['src'])
            filepath = 'url/{0}.{1}'.format(n, 'jpg')  # 文件路径
            with open(filepath, 'wb') as f:  # 打开文件
                f.write(img_res.content)
            n += 1
            print img_res


if __name__ == '__main__':
    get_dog()

# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from urlparse import urljoin
import requests
import csv
import re

# beijing
# bei_url = "http://bj.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000"

# guangzhou
guang_url = "http://gz.58.com/pinpaigongyu/pn/{page}?minprice=1000_1500&PGTID=0d3111f6-0000-34db-3e52-7fb9af6bb37c&ClickID=1"

page = 0

csv_file = open("guang_rent.csv","wb")
csv_writer = csv.writer(csv_file,delimiter=',')

while True:
    page += 1
    print "fetch: ",guang_url.format(page=page)
    response = requests.get(guang_url.format(page=page))
    html = BeautifulSoup(response.text, 'lxml')
    house_list = html.select(".list > li")

    if not house_list:
        break
    for house in house_list:
        house_title = house.select("h2")[0].string.encode("utf8")
        house_url = urljoin(guang_url, house.select("a")[0]["href"])
        house_info_list = house_title.split() 
        if "公寓" in house_info_list[1] or "青年社区" in house_info_list[1]:
            house_location = house_info_list[0]
        else:
            house_location = house_info_list[1]

        house_money = house.select(".money")[0].select("b")[0].string.encode("utf8")
        csv_writer.writerow([house_title,house_location,house_money,house_url])
csv_file.close()

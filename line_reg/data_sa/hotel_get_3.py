# -*- coding:utf-8 -*-
# ------------------------------
# @Time     :2019/5/10 17:26
# @Author   :jonie
# @Email    :joniea@qq.com
# @File     :hotel_get.py
# Description:
# ------------------------------
# -*- coding:utf-8 -*-
# ------------------------------
# @Time     :2019/5/9 13:32
# @Author   :jonie
# @Email    :joniea@qq.com
# @File     :code_get.py
# Description:
# ------------------------------
import csv
import json
import time
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen, quote
import json
import requests
# [113.63095213159264, 34.74830559988335]#
origin_path = '3 star hotel list.csv'  # 原始数据文件路径


machine_data = csv.reader(open(origin_path, 'r', encoding='utf-8'))  # 读取原始文件数据


for addr in machine_data:  # 循环爬取每一条数据
    # print(addr[2])


    address = addr[4]
    print(address)
    ak = 'FA8atAaqd1wajikD56lPqtiaNCleCeyz'
    url = 'http://api.map.baidu.com/geocoder/v2/?address='
    output = 'json'
    # ak = '你的ak'#需填入自己申请应用后生成的ak
    add = quote('郑州市'+address)  # 本文城市变量为中文，为防止乱码，先用quote进行编码
    url2 = url + add + '&output=' + output + "&ak=" + ak
    req = urlopen(url2)
    res = req.read().decode()
    temp = json.loads(res)
    lng = temp['result']['location']['lng']  # 获取经度
    lat = temp['result']['location']['lat']  # 获取纬度
    lng = ("%.5f" % lng)
    lat = ("%.5f" % lat)


    list1 = [lng, lat,addr[1]]
    print('百度坐标为：', list1)




    with open("3star酒店信息.csv", 'a', newline='',encoding='utf-8') as t:  # numline是来控制空的行数的
        writer = csv.writer(t)  # 这一步是创建一个csv的写入器（个人理解）
        writer.writerow(list1)  # 写入标签
        # writer.writerows(n)  # 写入样本数据
        t.close()


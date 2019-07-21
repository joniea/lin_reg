# -*- coding:utf-8 -*-
# ------------------------------
# @Time     :2019/5/10 20:06
# @Author   :jonie
# @Email    :joniea@qq.com
# @File     :data_select.py
# Description:
# ------------------------------
import time
import numpy as np
import csv


# origin_path = 'data/sort_line_sum1.csv'  # 原始数据文件路径
#
# val=0
# line_data = csv.reader(open(origin_path, 'r', encoding='utf-8'))  # 读取原始文件数据
# # print(line_data)
# for addr in line_data:  # 循环爬取每一条数据
#     # print(addr)
#     if int(addr[7])>2400:
#         val=addr[1]
#     else:
#         if addr[1]==val:
#             pass
#         else:
#             with open("data/排序后数据1.csv", 'a', newline='', encoding='utf-8') as t:  # numline是来控制空的行数的
#                 writer = csv.writer(t)  # 这一步是创建一个csv的写入器（个人理解）
#                 writer.writerow(addr)  # 写入标签
#                 # writer.writerows(n)  # 写入样本数据
#                 t.close()
# line_data1 = csv.reader(open("data/排序后数据1.csv", 'r', encoding='utf-8'))  # 读取原始文件数据
# vd=0
# num1=0
# lis=[]
# for addd in line_data1:  # 循环爬取每一条数据
#     if int(addd[7])<2400:
#         vd=addd[1]
#         lis.append(addd)
#
#     if addd[1]==vd :
#         num1 += 1
#     else:
#         pass
#     if num1==9:
#         num1=0
#         print(lis)
#
#         with open("data/排序后数据2.csv", 'a', newline='', encoding='utf-8') as d:  # numline是来控制空的行数的
#             writer = csv.writer(d)  # 这一步是创建一个csv的写入器（个人理解）
#
#             writer.writerow(lis)  # 写入标签
#             # writer.writerows(n)  # 写入样本数据
#             d.close()
#
#
#
#     else:
#         lis.clear()
#



    # print(addd)
    # if addd[1] == val:
    #     pass
    # else:
    #     with open("data/排序后数据2.csv", 'a', newline='', encoding='utf-8') as d:  # numline是来控制空的行数的
    #         writer = csv.writer(d)  # 这一步是创建一个csv的写入器（个人理解）
    #         writer.writerow(addd)  # 写入标签
    #         # writer.writerows(n)  # 写入样本数据
    #         d.close()

    # # print(addr[5])
    # print(addr[7])

# line_data = open(origin_path,'r', encoding='utf-8')
# line_data_dir = line_data.read().splitlines()
#
# for i in range(0, 3):
#     print(line_data_dir[i])
# line_data1 = csv.reader(open("data/排序后数据1.csv", 'r', encoding='utf-8'))  # 读取原始文件数据
# for addd in line_data1:  # 循环爬取每一条数据
#     num1=0
#     line_data2 = csv.reader(open("data/排序后数据1.csv", 'r', encoding='utf-8'))  # 读取原始文件数据
#     for ad in line_data2:
#         if ad[1]==addd[1]:
#             num1+=1
#         if num1 ==9:
#             with open("data/排序后数据2.csv", 'a', newline='', encoding='utf-8') as d:  # numline是来控制空的行数的
#                 writer = csv.writer(d)  # 这一步是创建一个csv的写入器（个人理解）
#                 writer.writerow(addd)  # 写入标签
#                 # writer.writerows(n)  # 写入样本数据
#                 d.close()



line_data1 = csv.reader(open("data/排序后数据1.csv", 'r', encoding='utf-8'))  # 读取原始文件数据
vd=0
num1=0
lis=[]
for addd in line_data1:  # 循环爬取每一条数据
    if int(addd[7])<=2400:
        vd=addd[1]
        print(addd)
        lis.append(addd)
        print("a",lis)
    if addd[1]==vd :
        num1 += 1
        print(num1)
    else:
        lis.clear()
        print("cl",lis)
        print(lis)
    if num1==9:

        print(lis)
        print(num1)
    #
        with open("data/排序后数据2.csv", 'a', newline='', encoding='utf-8') as d:  # numline是来控制空的行数的
            writer = csv.writer(d)  # 这一步是创建一个csv的写入器（个人理解）
            print(lis)
            writer.writerow(lis)  # 写入标签
            # writer.writerows(n)  # 写入样本数据
            d.close()
        lis.clear()
        num1 = 0






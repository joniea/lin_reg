# -*- coding:utf-8 -*-
# ------------------------------
# @Time     :2019/5/11 10:57
# @Author   :jonie
# @Email    :joniea@qq.com
# @File     :sorted_result.py
# Description:
# ------------------------------
import csv
hotel_list = []
line_data1 = csv.reader(open("工作簿1.csv", 'r', encoding='utf-8'))  # 读取原始文件数据
for hotel in line_data1:
    hotel_list.append(hotel[0])
n = 0
for i in range(0, len(hotel_list)):

    line_data2 = csv.reader(open("总体路程和时间详细.csv", 'r', encoding='utf-8'))  # 读取原始文件数据

    for data in line_data2:

        # print(data[1])
        # print(data[7])
        # print(hotel_list[i])
        if data[1] == hotel_list[i]:
            n+=1
            # print(data[7])
            with open("前34444汇总信息详细.csv", 'a', newline='', encoding='utf-8') as d:  # numline是来控制空的行数的
                writer = csv.writer(d)  # 这一步是创建一个csv的写入器（个人理解）

                writer.writerow(data)  # 写入标签
                # writer.writerows(n)  # 写入样本数据
                d.close()
print(n)

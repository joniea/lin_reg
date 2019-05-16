# -*- coding:utf-8 -*-
# ------------------------------
# @Time     :2019/5/9 20:15
# @Author   :jonie
# @Email    :joniea@qq.com
# @File     :tes1.py
# Description:
# 原数据文件格式csv： 起点纬度 + 起点经度 + 索引 + 终点纬度 + 终点经度
import csv
# origin_path_jiudian = '酒店信息.csv'  # 原始数据文件路径
origin_path_point = '赛点信息.csv'  # 原始数据文件路径
# address_jiudian = csv.reader(open(origin_path_jiudian, 'r', encoding='utf-8'))  # 读取原始文件数据
address_point = csv.reader(open(origin_path_point, 'r', encoding='utf-8'))  # 读取原始文件数据
file_train_dir = open('酒店信息.csv', encoding='utf-8')
# file_train_dir = open(os.path.join(DIR_SAMPLES, list_samples_dir[each_sample], NAME_TRAIN_DIR))
list_train_dir = file_train_dir.read().splitlines()
print(len(list_train_dir))
for each_train_dir in range(0, len(list_train_dir)):
    address_point = csv.reader(open(origin_path_point, 'r', encoding='utf-8'))  # 读取原始文件数据
    for point in address_point:
        print(list_train_dir[each_train_dir])






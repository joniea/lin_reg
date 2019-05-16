import csv

hotel_list = []
line_data1 = csv.reader(open("酒店信息.csv", 'r', encoding='utf-8'))  # 读取原始文件数据
for hotel in line_data1:

    hotel_list.append(hotel[2])
# print(hotel_list)
# print(len(hotel_list))
# line_data2 = csv.reader(open("酒店信息.csv", 'r', encoding='utf-8'))  # 读取原始文件数据
n = 0
for i in range(0, len(hotel_list)):
    num = 0
    sum1 = 0
    line_data2 = csv.reader(open("result_34_line.csv", 'r', encoding='utf-8'))  # 读取原始文件数据

    for data in line_data2:

        # print(data[1])
        # print(data[7])
        # print(hotel_list[i])
        if data[1] == hotel_list[i]:
            # print(data[7])
            if int(data[7]) < 2400:
                num += 1
                sum1 = sum1 + int(data[7])
    if num == 9:
        print([hotel_list[i], sum1])
        n += 1
        print(n)
        with open("result.csv", 'a', newline='', encoding='utf-8') as d:  # numline是来控制空的行数的
                writer = csv.writer(d)  # 这一步是创建一个csv的写入器（个人理解）

                writer.writerow([hotel_list[i],sum1])  # 写入标签
                # writer.writerows(n)  # 写入样本数据
                d.close()


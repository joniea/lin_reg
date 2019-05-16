from pyecharts import Bar
# import pycharts

#
# bar = Bar("我的第一个图表", "这里是副标题")
# bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90],is_more_utils=True)
# bar.show_config()
# bar.render()
# print(bar)
import sys
import csv
hotel_list = []
line_data1 = csv.reader(open("工作簿1.csv", 'r', encoding='utf-8'))  # 读取原始文件数据
for hotel in line_data1:
    hotel_list.append(float(hotel[1]))
print(hotel_list)
d2 = [c//540 for c in hotel_list]
print(d2)
v1 = d2


hotel_list2 = []
line_data2 = csv.reader(open("工作簿1.csv", 'r', encoding='utf-8'))  # 读取原始文件数据
for hotel in line_data2:
    hotel_list2.append(hotel[0])
print(hotel_list2)

v2 = hotel_list2


bar = Bar("我的第一个图表", "这里是副标题",title_color='red',  title_pos='right', width=1400, height=700)
bar.add("服装", v2, v1,is_dazoom=True ,width=1500,xaxis_rotate=90)
bar.show_config()
bar.render()
print(bar)



# attr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"] # 指定X轴刻度名字
# from pyecharts import Bar
# bar =Bar("标记线和标记点示例","副标题:展示每一维度数据的最小，最大，平均值")
# bar.add("商家A", attr, v1,mark_line=["min","average", "max"])
# bar.add("商家B", attr, v2, mark_line=["min","average", "max"])
# bar.render()
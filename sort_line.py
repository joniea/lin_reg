import csv
import re
import time
import json
from urllib.request import urlopen


# 百度地图提供的api服务网址
url_drive = r"http://api.map.baidu.com/direction/v2/driving"  # 驾车(routematrix 批量算路)
url_ride = r'http://api.map.baidu.com/routematrix/v2/riding?output=json'  # 骑行
url_walk = r'http://api.map.baidu.com/routematrix/v2/walking?output=json'  # 步行
url_bus = r'http://api.map.baidu.com/direction/v2/transit?output=json'  # bus(direction路线规划)
cod = r"&coord_type=bd09ll"
# 声明坐标格式,bd09ll(百度经纬度坐标);bd09mc(百度摩卡托坐标);gcj02(国测局加密坐标),wgs84(gps设备获取的坐标)
# AK为从百度地图网站申请的秘钥,额度不够的时候直接在list后面新增AK就行
AK = ['GSFM65oo6UVetxL7dt1zBdRl5HVFVbKG']


# 原数据文件格式csv： 起点纬度 + 起点经度 + 索引 + 终点纬度 + 终点经度
origin_path_jiudian = 'data/酒店信息.csv'  # 原始数据文件路径
origin_path_point = 'data/赛点信息.csv'  # 原始数据文件路径
result_path = 'data/result_34_sored_line.txt'  # 爬取数据文件保存路径


colnames = '设备序列号 起点 终点 状态码  路程(米) 耗时(秒)'
with open(result_path, 'a', encoding='utf-8') as f:
    f.write(colnames)
    f.write('\n')
    f.close()
address_jiudian = csv.reader(open(origin_path_jiudian, 'r', encoding='utf-8'))  # 读取原始文件数据

n = 0
akn1 = 0
akn2 = 0
a = 0

while True:
    try:  # 避开错误：文件编码问题、服务器响应超时、

        for ad in address_jiudian:
            address_point = csv.reader(open(origin_path_point, 'r', encoding='utf-8'))  # 读取原始文件数据
            for point in address_point:

                if (akn1 < len(AK)) and (akn2 < len(AK)):  # 配额是否够
                    mac_code = str(ad[2]+"-"+point[2])  # 设备序列号
                    try:
                        ori = str(ad[1]) + ',' + str(ad[0])  # 起点
                        des = str(point[1]) + ',' + str(point[0])  # 终点
                        ak_drive = AK[akn1]
                        ak_bus = AK[akn2]
                        ak_drive2 = r'&ak=' + ak_drive
                        ak_bus2 = r'&ak=' + ak_bus
                        ori1 = r"?origin=" + ori
                        des1 = r"&destination=" + des
                        # 以下是自驾车
                        tac_type = r'&tactics=11'  # 驾车路径:常规路线
                        # 10不走高速;11常规路线;12距离较短;13距离较短(不考虑路况)   只对驾车有效
                        aurl_drive = url_drive + ori1 + des1 + cod + tac_type + ak_drive2  # 驾车规划网址
                        # print(aurl_drive)
                        res_drive = urlopen(aurl_drive)  # 打开网页
                        cet_drive = res_drive.read()  # 解析内容
                        res_drive.close()  # 关闭
                        result_drive = json.loads(cet_drive)  # json转dict
                        status = result_drive['status']
                        # print('驾车码', status)
                        if status == 0:  # 状态码为0：无异常
                            m_drive = result_drive['result']["routes"][0]['distance']  # 里程(米)
                            m_drive2 = float(m_drive)  # str转float
                            timesec_drive = result_drive['result']["routes"][0]['duration']  # 耗时(秒)
                            diss_drive = '状态' + str(status), str(m_drive), str(timesec_drive)
                            # diss_drive = '状态' + str(status) + ' ' + str(m_drive) + ' ' + str(timesec_drive)  # 驾车总
                        elif status == 302 or status == 210 or status == 201:  # 302:额度不足;210:IP验证未通过
                            m_drive2 = 10000  # 赋值(大于5km),即不爬取步行规划
                            akn1 += 1
                            diss_drive = '状态' + str(status) + ' break break'
                        else:
                            m_drive2 = 10000  # 赋值(大于5km),即不爬取步行规划
                            diss_drive = '状态' + str(status) + ' na na'
                        try:  # 当驾车规划m_drive2为空的时候，if语句发生错误
                            if 0 < m_drive2 < 5000:  # 里程低于5公里则爬取步行规划
                                aurl_walk = url_walk + ori1 + des1 + cod + ak_drive2  # 步行规划网址
                                res_walk = urlopen(aurl_walk)  # 打开网页
                                cet_walk = res_walk.read()  # 解析内容
                                result_walk = json.loads(cet_walk)  # json转dict
                                res_walk.close()  # 关闭网页
                                status_walk = result_walk['status']  # 状态码
                                if status_walk == 0:  # 状态正常
                                    m_walk = result_walk['result']["routes"][0]['distance']  # 步行距离
                                    time_walk = result_walk['result']["routes"][0]['duration']  # 步行时间
                                    diss_walk = str(m_walk) + ' ' + str(time_walk)  # 步行总
                                else:  # 状态异常
                                    diss_walk = 'na na'
                            else:  # 里程大于5km则不爬取步行规划
                                diss_walk = 'na na'
                        except:  # 发生错误时步行数据也赋值为na
                            diss_walk = 'na na'
                            pass
                        # 以下是乘车规划
                        tac_bus = r'&tactics_incity=0'
                        # 市内公交换乘策略 可选，默认为0      0推荐；1少换乘；2少步行；3不坐地铁；4时间短；5地铁优先
                        city_bus = r'&tactics_intercity=0'
                        # 跨城公交换乘策略  可选，默认为0    0时间短；1出发早；2价格低；
                        city_type = r'&trans_type_intercity=2'
                        # 跨城交通方式策略  可选，默认为0  0火车优先；1飞机优先；2大巴优先；
                        ori2 = r"&origin=" + ori
                        des2 = r"&destination=" + des
                        aurl_bus = url_bus + ori2 + des2 + tac_bus + city_bus + city_type + ak_bus2
                        res_bus = urlopen(aurl_bus)
                        cet_bus = res_bus.read()
                        res_bus.close()
                        result_bus = json.loads(cet_bus)
                        status = result_bus['status']
                        # print('乘车码', status)
                        # --------------------------------------
                        # if status == 0:
                        #     rsls = result_bus['result']['routes']
                        #     if rsls == []:  # 无方案时状态也为0，但只返回一个空list
                        #         diss_bus = '状态' + str(status) + ' ' + '无公交方案'
                        #     else:
                        #         m_bus = result_bus['result']['routes'][0]['distance']  # 乘车路线距离总长(米)
                        #         time_bus = result_bus['result']['routes'][0]['duration']  # 乘车时间(秒)
                        #         cost_bus = result_bus['result']['routes'][0]['price']  # 乘车费用(元)
                        #         diss_bus = '状态' + str(status) + ' ' + str(m_bus) + ' ' + str(time_bus) + ' ' + str(cost_bus)
                        # elif status == 302 or status == 210 or status == 201:
                        #     akn2 = akn2 + 1
                        #     diss_bus = '状态' + str(status) + ' ' + '更换AK断点'
                        # else:  # 其他类型状态码(服务器错误)
                        #     diss_bus = '状态' + str(status) + ' ' + '服务器错误'
                        #     -----------------------------------------------
                        # 汇总数据
                        diss=[mac_code,ad[2],point[2],str(ori),str(des),diss_drive,diss_walk]
                        # diss = mac_code + str("\t")+' ' + str(ori) + ' ' + str(
                        #     des) + ' ' + diss_drive + ' ' + diss_walk #+ ' ' + diss_bus
                        with open(result_path, 'a', encoding='utf-8') as f:
                            f.write(str(diss))
                            f.write('\n')
                            f.close()
                        with open("data/result_34_sored_line.csv", 'a', newline='', encoding='utf-8') as t:  # numline是来控制空的行数的
                            writer = csv.writer(t)  # 这一步是创建一个csv的写入器（个人理解）
                            writer.writerow(diss)  # 写入标签
                            # writer.writerows(n)  # 写入样本数据
                            t.close()
                        n += 1
                        print('第' + str(n) + '条已完成')

                    except:
                        time.sleep(3)
                        diss_wrong = str(mac_code) + '未知错误'
                        with open(result_path, 'a', encoding='utf-8') as f:
                            f.write(diss_wrong)
                            f.write('\n')
                            f.close()
                        continue
                else:
                    print('配额不足！')
                    break
    except:
        time.sleep(3)
        print('未知错误')
        with open(result_path, 'a', encoding='utf-8') as f:
            f.write('未知错误')
            f.write('\n')
            f.close()
        continue
    print('程序已停止运行')
    break  # 跑完数时break打断while循环,for循环的话这里不好定义循环条件



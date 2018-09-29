#"coding=utf-8"
import time
import torndb
import numpy
from math import *
import json
db = torndb.Connection(host = 'localhost',database ='weather',user = 'root',password = '123456')

#获取指定站点全部信息
def get_info(station):
    try:
        sid=station
        sql="select * from station where sid=%s"%(sid)
        sinfo=db.query(sql)
        sql2="select * from s%s"%(sid)
        sweather=db.query(sql2)
        data=sinfo+sweather
        # print data
    except:
        data=[]
    return data

#获取指定站点天气，用于画图，返回：1【高度，温度】、2【高度，风速】
#3【高度，风向】、4【高度，气压】
def get_selected_json(sid,flag):
    if(flag==1):
        value='temp'
    elif(flag==2):
        value='sknt'
    elif(flag==3):
        value='drct'
    else:
        value='pres'
    try:
        sql='select hght,%s from s%s order by hght ASC'%(value,sid)
        re=db.query(sql)
        data=[]
        for r in re:
            t=[]
            t.append(float(r['hght']))
            t.append(float(r[value]))
            data.append(t)
        #print data
        data.sort()#排序，升序，hcharts绘图需要
        # print data
        return data
    except:
        data=[]
        return data

#获取某个站点信息，只获取站点信息，没有天气信息
def get_station_info(sid):
    sql='select * from station where sid=%s'%(sid)
    res=db.query(sql)
    return  res


#获取某个站点的高度、风向、风速，返回格式 {高度1:[风向1,风速1]，高度2:[风向2,风速2]...}， 顺序依前
def get_station_wind(sid):
    sql='select hght,drct,sknt from s%s'%(sid)
    res=db.query(sql)
    t={}
    for r in res:
        tt=[]
        tt.append(r['drct'])
        tt.append(r['sknt'])
        t[r['hght']]=tt
    # print t
    # print t.keys()
    # print t['791']
    return t

#反切函数，规整数据
def math_translate(x):
    return (8/numpy.pi)*numpy.arctan(x)


##获取指定站点天气，用于画图，返回：1【高度，温度】、2【高度，风速】
#3【高度，风向】、4【高度，气压】
'''
在上述基础上，对数据进行处理，使其在(-4,4),反切函数：(8/pi)*arctan(x)
'''
def get_computed_json(sid,flag):
    if(flag==1):
        value='temp'
    elif(flag==2):
        value='sknt'
    elif(flag==3):
        value='drct'
    else:
        value='pres'
    try:
        sql='select hght,%s from s%s order by hght ASC'%(value,sid)
        re=db.query(sql)
        data=[]
        for r in re:
            t=[]
            t.append(math_translate(float(r['hght'])))
            t.append(math_translate(float(r[value])))
            data.append(t)
        #print data
        data.sort()#排序，升序，hcharts绘图需要
        # print data
        return data
    except:
        data=[]
        return data


#获取所有站点的告警信息，返回格式: {'51777':1,'56885':0,...}
def get_warning_info():
    sql='select sid,warning from station'
    re=db.query(sql)
    t={}
    for r in re:
        t[r['sid']]=r['warning']
    # print t
    return t
# 获取所有告警站点的经纬度
def get_warning_pos():
    sql='select longitude,latitude from station where warning<>0'
    res=db.query(sql)
    data=[]
    for r in res:
        t=[]
        t.append(r['longitude'])
        t.append(r['latitude'])
        data.append(t)
    return data


#两经纬度之间的距离
def haversine(lon1, lat1, lon2, lat2): # 经度1，纬度1，经度2，纬度2 （十进制度数）
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # 地球平均半径，单位为公里
    return c * r


#传入经纬度，按照就近原则，返回最靠近的一个站点代码
def loc2sta(lo,la):
    sql="select sid,longitude,latitude from station"
    res=db.query(sql)
    tar_station=''
    min_len=1000000
    for r in res:
        length=haversine(lo,la,float(r['longitude']),float(r['latitude']))
        # print r['sid'],length
        if(length<min_len):
            tar_station=r['sid']
            min_len=length
    return tar_station

#选择某高度的天气（就近）
def select_height(data,h):
    min_distance=1000000
    near={}
    for i in range(1,len(data)):
        td=abs(int(data[i]['hght'])-h)
        if td<min_distance:
            min_distance=td
            near=data[i]
    # print near
    return near

#传入经纬度和高度，得到天气,并拼接成一条神经网络输入数据
def loc2wea(lon,lat,hgt,pdrct,pweight):
    sid=loc2sta(float(lon),float(lat)) #由经纬度，得到最靠近的一个站点的站点代码
    data=select_height(get_info(sid),int(hgt)) #由最近的站点的天气信息，结合飞机的高度，给出最近高度层的信息
    x=[]
    x.append(float(data['temp'])*0.01)
    x.append(float(data['pres'])*0.01)
    x.append(float(data['drct'])*0.01)
    x.append(float(data['sknt'])*0.01)
    x.append(float(pdrct)*0.01)
    x.append(float(pweight)*0.01)
    return x

def path_weather(path):
    res=[]
    for r in path:
        t=loc2wea(r[0],r[1],r[2],r[3],r[4])
        res.append(t)
    return res




'''
此处测试完记得注释！！！
否则会造成服务模块调用功能函数出现异常
'''
# get_info('58238')
# select_height(get_info('58238'),800)
# get_selected_json('58238',1)
# get_station_wind('58665')
# get_warning_info()
# get_computed_json('58665',1)
# loc2sta(108.21,39.48)
# get_warning_pos()
# path=[['125','49','1000','200','500'],['126','45','900','200','500'],['88','47','800','200','500']]
# path_weather(path)
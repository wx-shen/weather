#"coding=utf-8"
import threading
import requests
import re
import time
import datetime
import torndb
SLEEP_TIME = 1
resource=[]#暂存各站点数据
con_pool=[]#数据库连接资源池
flag={}#标记站点是否被清空
warnig_flag={}#记录站点的警告代码
adb = torndb.Connection(host = 'localhost',database ='weather',user = 'root',password = '123456')
#获取当前时间
def gettime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

#初始化数据库连接资源池,n为制定的最大连接数
def init_con_pool(n):
    for i in range(0,n):
        tdb=torndb.Connection(host = 'localhost',database ='weather',user = 'root',password = 'testpassword')
        con_pool.append(tdb)


#清除表中信息，用于更新表之前
def clear_table(name,db):
    t=gettime()
    sid=name[1:len(name)]
    sql='truncate table %s'%(name)
    sql2="update station set updatetime='%s' where sid=%s"%(t,sid)
    sql3='update station set warning=%s where sid=%s'%(warnig_flag[name],sid)
    db.execute(sql)
    db.execute(sql2)
    db.execute(sql3)

#数据库交互函数
def save(station,pres,hght,temp,drct,sknt,db):
    sql='insert into %s (pres,hght,temp,drct,sknt) values(%s,%s,%s,%s,%s)'%(station,pres,hght,temp,drct,sknt)
    db.execute(sql)


#数据库数据存入
def write2db():
    while(True):
        if(len(con_pool)):
            db=con_pool.pop()#若连接资源池中有连接资源，取一个连接，否则等待
            break

    while(True):
        if(resource): #检测到内存缓存区有数据，进入处理
            while(resource):
                t=resource.pop()
                if(flag[t['station']]==0): #该站点信息未被清空，则清空
                    station=t['station']
                    clear_table(station,db)#清空表，不可恢复
                    flag[t['station']]=1
                save(t['station'],t['pres'],t['hght'],t['temp'],t['drct'],t['sknt'],db)
                print 'resource-length:'+str(len(resource))
            #print flag
            break    #全部处理完毕

#数据库多线程写入
def multi_write2db(max):
    threads=[]
    while threads or len(resource):
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread) #移除非活跃线程
        while len(threads)<max and len(resource): #线程数未达到上限并且资源数缓冲区存在待写入的资源
            thread = threading.Thread (target=write2db)
            # 可以用ctrl-c退出
            thread.setDaemon (True)
            thread.start()
            threads.append(thread)
        time.sleep(SLEEP_TIME)
    # while(True):
    #     if(len(threads)==0):
    #         break




#getsource用来获取网页源代码
def getsource(url):
    try:
        html = requests.get(url,timeout=5)
    except:
        html=requests.get(url,timeout=8)#超时重连
        print 'reconnect success'
    if len(html.text)==0:#未抓取到页面
        try:
          html = requests.get(url,timeout=5)
        except:
          html=requests.get(url,timeout=8)#超时重连
          print 'reconnect success'
    return html.text

#geteveryclass用来抓取每个信息块
def geteveryclass(source):
    everyclass = re.findall('<PRE>(.*?)</PRE>',source,re.S)#正则匹配，返回数组
    if(len(everyclass)==0):
        everyclass = re.findall('<PRE>(.*?)</PRE>',source,re.S)
    return everyclass

#handle_data，将得到的字符串切割，归类，转变为数组，并存入数据库
def handle_data(station,info):
     if info=='':#抓取数据为空，即该站点暂无观测数据
         tem={}
         tem['station']=station
         tem['pres']='0'
         tem['hght']='0'
         tem['temp']='0'
         tem['drct']='0'
         tem['sknt']='0'
         resource.append(tem)
         return
     inforan=info.split('\n')
     length=len(inforan)
     for i in range(5,length-1):
         t=inforan[i].split()
         #print t
         pres=t[0]
         hght=t[1]
         temp=t[2]
         if(len(t)==11):
             drct=t[6]
             sknt=t[7]
         elif(len(t)>4):
             drct=t[3]
             sknt=t[4]
         else:
             continue
         #print station ,pres ,hght ,temp ,drct ,sknt
         tem={}
         tem['station']=station
         tem['pres']=pres
         tem['hght']=hght
         tem['temp']=temp
         tem['drct']=drct
         tem['sknt']=sknt
         name='s'+station
         if(float(temp)<-70):
             warnig_flag[name]=1 #记录温度异常
         elif(float(sknt)>80):
             warnig_flag[name]=2#记录风速异常
         resource.append(tem)#写入内存缓冲区

#所有站点信息，获取待爬取URL队列
def all_links():
    s=[]
    sql="select * from station"
    sran=adb.query(sql)
    for t in sran:
        sid=t['sid']
        s.append(sid)
    return s

#初始化标记字典，告警记录字典
def init_flag(f,ff):
    s=all_links()
    for t in s :
        st='s'+t
        f[st]=0
        ff[st]=0


#处理函数
def threaded_crawle(max_threads):
    sta=all_links()
    tim=gettime()[0:10].split('-')
    lin = 'http://weather.uwyo.edu/cgi-bin/sounding?region=seasia&TYPE=TEXT%3ALIST&'
    year='YEAR='+tim[0]
    month='&MONTH='+tim[1]
    day=tim[2]+'00'
    tag='&FROM='+day+'&TO='+day+'&STNM='
    lin+=year+month+tag
    def process_queue():
        while True:
            try:
                s=sta.pop()#取一个站点
            except IndexError:
                break #为空
            else:
                link=lin+s #拼接站点代码
                html =getsource(link)
                try:
                    everyclass = geteveryclass(html)
                    info=everyclass[0]
                except:
                    #未获取到数据,再次获取
                    print 'reget...'
                    try:
                        html =getsource(link)
                        everyclass = geteveryclass(html)
                        info=everyclass[0]
                    except:
                        try:
                            print 'reget again!'
                            html =getsource(link)
                            everyclass = geteveryclass(html)
                            info=everyclass[0]
                        except:
                            info=''#站点数据暂无
                            print 'fail get!'+link
                            st='s'+s
                            flag[st]=1  #当前站点数据不存在，则沿用旧数据，将标记设为1，不清空表
                station='s'+s
                print '#'+' '+station+' handling...'
                handle_data(station,info)
    threads=[]
    while threads or sta:
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread) #移除非活跃线程
        while len(threads)<max_threads and sta: #线程数未达到上线并且资源数组中存在待处理资源
            thread = threading.Thread (target=process_queue)
            # 可以用ctrl-c退出
            thread.setDaemon (True)
            thread.start()
            threads.append(thread)
        time.sleep(SLEEP_TIME)

def run_spiderx():
    starttime = datetime.datetime.now()
    init_flag(flag,warnig_flag)#初始化清空标记
    init_con_pool(5)#初始化数据库连接池
    threaded_crawle(10)  #爬虫
    # while (datathread.is_alive()): #等待数据线程结束
    #     time.sleep(2)
    multi_write2db(2)
    endtime = datetime.datetime.now()
    print (endtime-starttime).seconds

run_spiderx()



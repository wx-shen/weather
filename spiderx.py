#"coding=utf-8"
import threading
import requests
import re
import time
import datetime
import torndb
SLEEP_TIME = 1
resource=[]#暂存各站点数据
flag={}#标记站点是否被清空
warnig_flag={}#记录站点的警告代码
error=[]#用于记录抓取失败的站点
db = torndb.Connection(host = 'localhost',database ='weather',user = 'root',password = '123456')
#获取当前时间
def gettime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

#清除表中信息，用于更新表之前
def clear_table(name):
    t=gettime()
    sid=name[1:len(name)]
    sql='truncate table %s'%(name)
    sql2="update station set updatetime='%s' where sid=%s"%(t,sid)
    db.execute(sql)
    db.execute(sql2)


#存入站点告警信息
def update_warning(name,sid):
    sql3='update station set warning=%s where sid=%s'%(warnig_flag[name],sid)
    db.execute(sql3)



#数据库交互函数
def save(station,pres,hght,temp,drct,sknt):
    sql='insert into %s (pres,hght,temp,drct,sknt) values(%s,%s,%s,%s,%s)'%(station,pres,hght,temp,drct,sknt)
    db.execute(sql)


#数据库数据存入
def write2db():
    while(True):
        if(resource): #检测到内存缓存区有数据，进入处理
            while(resource):
                t=resource.pop()
                if(flag[t['station']]==0): #该站点信息未被清空，则清空
                    station=t['station']
                    clear_table(station)#清空表，不可恢复
                    flag[t['station']]=1
                name=t['station']
                update_warning(name,name[1:len(name)])
                save(t['station'],t['pres'],t['hght'],t['temp'],t['drct'],t['sknt'])
                print '内存缓冲区数据长度:'+str(len(resource))
            #print flag
            break    #全部处理完毕


#getsource用来获取网页源代码
def getsource(url):
    try:
        html = requests.get(url,timeout=5)
    except:
        html=requests.get(url,timeout=8)#超时重连
        print '重连成功'
    if len(html.text)==0:#未抓取到页面
        try:
          html = requests.get(url,timeout=5)
        except:
          html=requests.get(url,timeout=8)#超时重连
          print '第二次重连成功'
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
         elif(len(t)>5):
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
         if(float(temp)<-70):
             if(warnig_flag[station]==2 or warnig_flag[station]==3):
                 warnig_flag[station]=3 #双重告警
             else:
                 warnig_flag[station]=1 #记录温度异常
         if(float(sknt)>70):
             if(warnig_flag[station]==1 or warnig_flag[station]==3):  #已经被记录有告警
                 warnig_flag[station]=3
             else:
                 warnig_flag[station]=2#记录风速异常
         resource.append(tem)#写入内存缓冲区

#所有站点信息，获取待爬取URL队列
def all_links():
    s=[]
    sql="select * from station"
    sran=db.query(sql)
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
                    print '重新提取...'
                    try:
                        html =getsource(link)
                        everyclass = geteveryclass(html)
                        info=everyclass[0]
                    except:
                        try:
                            print '第二次重取!'
                            html =getsource(link)
                            everyclass = geteveryclass(html)
                            info=everyclass[0]
                        except:
                            info=''#站点数据暂无
                            print u'未获得!'+link
                            st='s'+s
                            flag[st]=1  #当前站点数据不存在，则沿用旧数据，将标记设为1，不清空表
                            warnig_flag[st]=-1
                            error.append(link)
                station='s'+s
                print u'站点'+' '+station+u'正在处理...'
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

#处理多线程爬虫未抓取到的链接,为单线程写入，避免服务器来不及响应
def handle_error(error):
    while True:
            try:
               link=error.pop()#取一个链接
               s=link[-5:]
               station='s'+s
               warnig_flag[station]=0 #归0
            except IndexError:
                break #为空
            else:
                html =getsource(link)
                try:
                    everyclass = geteveryclass(html)
                    info=everyclass[0]
                except:
                    #未获取到数据,再次获取
                    print '重新提取...'
                    try:
                        html =getsource(link)
                        everyclass = geteveryclass(html)
                        info=everyclass[0]
                    except:
                        try:
                            print '第二次重新提取!'
                            html =getsource(link)
                            everyclass = geteveryclass(html)
                            info=everyclass[0]
                        except:
                            info=''#站点数据暂无
                            print u'第二次未获得站点!!'+link
                            st='s'+s
                            flag[st]=1  #当前站点数据不存在，则沿用旧数据，将标记设为1，不清空表
                            warnig_flag[station]=-1

                print u'站点'+' '+station+u' 重新抓取中..'
                handle_data(station,info)



def run_spiderx():
    starttime = datetime.datetime.now()
    init_flag(flag,warnig_flag)#初始化清空标记
    threaded_crawle(10)  #爬虫
    handle_error(error)
    datathread = threading.Thread(target=write2db)  # 启动内存数据写入线程
    datathread.setDaemon(True)
    datathread.start()
    while (datathread.is_alive()): #等待数据线程结束
        time.sleep(2)
    endtime = datetime.datetime.now()
    print (endtime-starttime).seconds
run_spiderx()



#"coding=utf-8"
import requests
import re
import time
import datetime
import torndb
db = torndb.Connection(host = 'localhost',database ='weather',user = 'root',password = 'testpassword')

#获取当前时间
def gettime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

#清除表中信息，用于更新表之前
def clear_table(name):
    sql='truncate table %s'%(name)
    db.execute(sql)

#数据库交互函数
def save(station,pres,hght,temp,drct,sknt):
    t=gettime()
    sid=station[1:len(station)]
    sql2="update station set updatetime='%s' where sid=%s"%(t,sid)
    sql='insert into %s (pres,hght,temp,drct,sknt) values(%s,%s,%s,%s,%s)'%(station,pres,hght,temp,drct,sknt)
    db.execute(sql)
    db.execute(sql2)


class spider(object):#定义一个爬虫类
    def __init__(self):
        print u'开始爬取内容。。。'


#getsource用来获取网页源代码
    def getsource(self,url):
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
    def geteveryclass(self,source):
        everyclass = re.findall('<PRE>(.*?)</PRE>',source,re.S)#正则匹配，返回数组
        if(len(everyclass)==0):
            everyclass = re.findall('<PRE>(.*?)</PRE>',source,re.S)
        return everyclass


#handle_data，将得到的字符串切割，归类，转变为数组，并存入数据库
    def handle_data(self,station,info):
         if info=='':
            save(station,'0','0','0','0','0')
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
             save(station,pres,hght,temp,drct,sknt)

#所有站点信息
def all_links():
    s=[]
    sql="select * from station"
    sran=db.query(sql)
    for t in sran:
        sid=t['sid']
        s.append(sid)
    return s


if __name__ == '__main__':
    starttime = datetime.datetime.now()
    weatherspider = spider()
    links=all_links()
    tim=gettime()[0:10].split('-')
    lin = 'http://weather.uwyo.edu/cgi-bin/sounding?region=seasia&TYPE=TEXT%3ALIST&'
    year='YEAR='+tim[0]
    month='&MONTH='+tim[1]
    day=tim[2]+'00'
    tag='&FROM='+day+'&TO='+day+'&STNM='
    lin+=year+month+tag
    count=0
    for t in links:
        link=lin
        link+=t
        #print link
        html =weatherspider.getsource(link)
        try:
            everyclass = weatherspider.geteveryclass(html)
            info=everyclass[0]
        except:
            #未获取到数据,再次获取
            print 'reget...'
            try:
                html =weatherspider.getsource(link)
                everyclass = weatherspider.geteveryclass(html)
                info=everyclass[0]
            except:
                try:
                    print 'reget again!'
                    html =weatherspider.getsource(link)
                    everyclass = weatherspider.geteveryclass(html)
                    info=everyclass[0]
                except:
                    info=''
                    print 'fail get!'+link
        station='s'+t
        count+=1
        print '#'+str(count)+' '+station+' handling...'
        clear_table(station)#清空表，不可恢复
        weatherspider.handle_data(station,info)
    endtime = datetime.datetime.now()
    print (endtime-starttime).seconds

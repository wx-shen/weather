#"coding=utf-8"
import torndb
db = torndb.Connection(host = 'localhost',database ='weather',user = 'root',password = 'testpassword')
sql="select * from station"
sran=db.query(sql)
s='['
re=[]
count=0
for t in sran:
    # sid=t['sid']
    # if(sid=='51777'):
    #     continue
    # tablename='s'+sid
    # sql2="create table %s like s51777"%(tablename)
    # db.execute(sql2)

    lon=t['longitude']
    lat=t['latitude']
    s+='["%s","%s"],'%(lon,lat)


    # sid=t['sid']
    # name=t['name']
    # s+='{"id":%s,"name":"%s","type":1},'%(sid,name)

    count+=1
    if(count%3==0):
        s+='\n'

print s
print count


# link = 'http://weather.uwyo.edu/cgi-bin/sounding?region=seasia&TYPE=TEXT%3ALIST&YEAR=2018&MONTH=02&FROM=0500&TO=0500&STNM=
# import requests
# url='http://weather.uwyo.edu/cgi-bin/sounding?region=seasia&TYPE=TEXT%3ALIST&YEAR=2018&MONTH=02&FROM=0500&TO=0500&STNM=45004
# res=requests.get(url)
# print res.text

# s='s52777'
# print s[1:len(s)]
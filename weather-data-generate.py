#"coding=utf-8"
import csv
import torndb
db = torndb.Connection(host = 'localhost',database ='weather',user = 'root',password = 'testpassword')
sql="select sid from station"
stres=db.query(sql)
# print sres
count=0
data=[]
for r in stres:
    sid=r['sid']
    sql2="select * from s%s"%(sid)
    sres=db.query(sql2)
    plan_weight=500
    plan_drct=200
    count+=1
    if(count==2):
        break
    for sr in sres:
        t=[]
        temp=float(sr['temp'])
        pres=float(sr['pres'])
        drct=float(sr['drct'])
        sknt=float(sr['sknt'])
        if(temp<-55 or sknt>100):
            status=-1
        else:
            status=1
        t.append('%.2f'%(temp*0.01))
        t.append('%.2f'%(pres*0.01))
        t.append('%.2f'%(drct*0.01))
        t.append('%.2f'%(sknt*0.01))
        t.append('%.2f'%(plan_drct*0.01))
        t.append('%.2f'%(plan_weight*0.01))
        t.append(status)
        data.append(t)
    # print data
    # print len(data)
with open("weather_data.csv", "wb+") as fw:
        writer = csv.writer(fw)
        for row in data:
            writer.writerow(row)
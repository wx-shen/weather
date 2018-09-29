#"coding=utf-8"
import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.options
import os.path
import json
import numpy
import sys
from tornado.options import define, options
from condb import *
from weather_neural import *
define("port", default=9000, type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class MapHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("map.html")


class ShowNeuralHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("neural-show.html")


class WeatherHandler(tornado.web.RequestHandler):
    def get(self,id):
        data=get_info(id)
        sinfo=data[0]
        winfo=data[1:]
        self.render('station-weather.html',sinfo=sinfo,winfo=winfo)


class RunHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*") #打开跨域访问
    def get(self,info):
        info=info.split('/')
        # print info
        eta=float(info[0])
        n=int(info[1])
        train(eta,n)
        self.write('success!')

class JudgeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('neural-judge.html')

class JudgeDataHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*") #打开跨域访问
    def get(self,info):
        mes=info.split('/')
        sid=loc2sta(float(mes[0]),float(mes[1])) #由经纬度，得到最靠近的一个站点的站点代码
        data=select_height(get_info(sid),int(mes[2])) #由最近的站点的天气信息，结合飞机的高度，给出最近高度层的信息
        neu=weather_neaural(eta=0.0001, n_iter=100,w_flag=1)
        x=[]
        x.append(float(data['temp'])*0.01)
        x.append(float(data['pres'])*0.01)
        x.append(float(data['drct'])*0.01)
        x.append(float(data['sknt'])*0.01)
        x.append(float(mes[3])*0.01)
        x.append(float(mes[4])*0.01)
        y=neu.predict(numpy.array(x)).tolist()
        if(y==1):
            status='safe'
        else:
            status='danger!'
        res=[]
        res.append(data['sknt'])
        res.append(data['drct'])
        res.append(data['temp'])
        res.append(data['pres'])
        res.append(status)
        # print json.dumps(res)
        self.write(json.dumps(res))

class RestshowHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('restapi-show.html')

class PathHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*") #打开跨域访问
    def get(self):
        self.render('path.html')
    def post(self):
        data = json.loads(self.request.body)
        w=path_weather(data)
        print w
        x=numpy.array(w) #将普w通list转换为num_array
        neu=weather_neaural(eta=0.0001, n_iter=100,w_flag=1)
        judge=neu.predict(x).tolist()
        danger=[]
        for i in range(0,len(judge)):
            t=[]
            if (judge[i]==1):
                t.append(data[i][0])
                t.append(data[i][1])
            danger.append(t)
        mes=json.dumps(danger)
        # print mes
        self.write(mes)



#主运行
if __name__ == "__main__":
    settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "pn6OqYE4RNi012c1pcF26gbDQTiEA07Ynniqz+TGyAw=",
    "xsrf_cookies": False, #开启伪造POST请求防护功能
    "login_url": "/login"
    }
    #路由表
    Handlers = [(r'/',IndexHandler),
                (r'/(\d+)', WeatherHandler),
                (r'/map',MapHandler),
                (r'/neural',ShowNeuralHandler),
                (r'/run/(.*?)',RunHandler),
                (r'/judge',JudgeHandler),
                (r'/judge_data/(.*?)',JudgeDataHandler),
                (r'/rest',RestshowHandler),
                (r'/path',PathHandler)
              ]
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=Handlers, **settings )
    http_sever = tornado.httpserver.HTTPServer(app)
    http_sever.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
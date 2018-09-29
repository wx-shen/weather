#"coding=utf-8"
import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.options
import os.path
from tornado.options import define, options
from condb import *
define("port", default=9002, type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self,info):
        #接受一个经纬度和高度，就近寻找一个站点，并返回该站点的该高度（就近）的天气数据
        s=info.split('/')
        longitude=s[0]
        latitude=s[1]
        h=s[2]
        station=loc2sta(float(longitude),float(latitude))#依据经纬度得到站点代码
        tdata=get_info(station)                         #依据站点代码得到站点天气数据
        data=select_height(tdata,int(h))                #依据飞行器实际高度得到相应的天气数据
        self.write(data)



#主运行
if __name__ == "__main__":
    settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "pn6OqYE4RNi012c1pcF26gbDQTiEA07Ynniqz+TGyAw=",
    "xsrf_cookies": True, #开启伪造POST请求防护功能
    "login_url": "/login"
    }
    #路由表
    Handlers = [ (r'/(.*?)',IndexHandler)
              ]
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=Handlers, **settings )
    http_sever = tornado.httpserver.HTTPServer(app)
    http_sever.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
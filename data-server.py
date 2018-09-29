#"coding=utf-8"
import tornado.ioloop
import pyrestful.rest
from pyrestful import mediatypes
from pyrestful.rest import get
from condb import *

class Alldata(pyrestful.rest.RestHandler):
      def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*") #打开跨域访问
      @get(_path="/weather/{station}", _produces=mediatypes.APPLICATION_JSON)
      def weather(self, station):
           data=get_info(station)
           return data

      #获取温度，可选参数：0，未经数学规整；1：经过反切函数规整
      @get(_path="/weather/{station}/temp/{type}", _produces=mediatypes.APPLICATION_JSON)
      def temp(self, station,type):
          if(type=='0'):
              data=get_selected_json(station,1)
          elif(type=='1'):
              data=get_computed_json(station,1)
          else:
              data=[]
          return data

      #获取风速，可选参数：0，未经数学规整；1：经过反切函数规整
      @get(_path="/weather/{station}/sknt/{type}", _produces=mediatypes.APPLICATION_JSON)
      def sknt(self, station,type):
          if(type=='0'):
              data=get_selected_json(station,2)
          elif(type=='1'):
              data=get_computed_json(station,2)
          else:
              data=[]
          return data

      #获取风向，可选参数：0，未经数学规整；1：经过反切函数规整
      @get(_path="/weather/{station}/drct/{type}", _produces=mediatypes.APPLICATION_JSON)
      def drct(self, station,type):
           if(type=='0'):
              data=get_selected_json(station,3)
           elif(type=='1'):
              data=get_computed_json(station,3)
           else:
              data=[]
           return data
      # 获取气压，可选参数：0，未经数学规整；1：经过反切函数规整
      @get(_path="/weather/{station}/pres/{type}", _produces=mediatypes.APPLICATION_JSON)
      def pres(self, station,type):
           if(type=='0'):
              data=get_selected_json(station,4)
           elif(type=='1'):
              data=get_computed_json(station,4)
           else:
              data=[]
           return data

      #获取指定站点站点信息
      @get(_path="/{station}", _produces=mediatypes.APPLICATION_JSON)
      def station_info(self, station):
           data=get_station_info(station)
           # print type(data)
           return data

      #获取某个站点的风向，风速
      @get(_path="/weather/{station}/wind", _produces=mediatypes.APPLICATION_JSON)
      def wind(self, station):
           data=get_station_wind(station)
           return data



      #获取所有站点的告警信息
      @get(_path="/weather/warning/{flag}", _produces=mediatypes.APPLICATION_JSON)
      def warning(self,flag):
           if(flag=='1'):
               data=get_warning_info()
           else:
               data=get_warning_pos()
           return data


if __name__ == '__main__':
      try:
           print("Start the echo service")
           app = pyrestful.rest.RestService(rest_handlers=[Alldata])
           app.listen(9001)
           tornado.ioloop.IOLoop.instance().start()
      except KeyboardInterrupt:
           print("\nStop the echo service")
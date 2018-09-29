#"coding=utf-8"
from spiderx import *
import time
'''
监控程序，用于启动爬虫脚本，更新数据库中的天气数据
'''
while(True):
    run_spiderx()
    print '数据更新完成于：'+time.strftime('%Y-%m-%d %X',time.localtime())
    # time.sleep(86400)#休眠一天，第二天再更新
    time.sleep(10)

#"coding=utf-8"
'''
天气情况判断神经网络
'''
import numpy as np
import pandas as pd
import sys
import csv
import webbrowser
import time
import websocket
import json
reload(sys)
sys.setdefaultencoding('utf-8') #编码问题,将读取外部文件默认为utf-8
class weather_neaural(object):
    """
    eta:float
    学习效率，处于0和1

    n_iter:int
    对训练数据进行学习改进次数

    w_:一维向量
    存储权重数值

    error_:
    存储每次迭代改进时，网络对数据进行错误判断的次数
    """

    def __init__(self, eta=0.01, n_iter=50,w_flag=0):   #w_falg用于记录是否需要读取W
        self.eta = eta
        self.n_iter = n_iter
        self.w_flag=w_flag
        if self.w_flag!=0:
            wcsv = pd.read_csv('weather_w.csv', header=None)
            self.w_=wcsv.loc[0:0].values[0]  #获取存储的w值，用于神经网络
        self.cost_ = []
        """
        X:shape,二维数组[n_samples, n_features]
        example: x:[[1,2,3],[4,5,6]]===>x:shape:[2,3]
        n_samples 表示X中含有训练数据条目数
        n_features 含有4个数据的一维向量，用于表示一条训练数目

        y:一维向量
        用于存储每一训练条目对应的正确分类
        """

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])

        """
        注意自在训练神经网络的时候，一次迭代就将取到的所有数据输入，往复输入，往复调整
        """
        for i in range(self.n_iter):
            output = self.net_input(X)
            errors = (y - output)
            # print '，errors：',
            # print errors
            self.w_[1:] += self.eta * X.T.dot(errors)  #X.T 转秩 ;dot,矩阵相乘
            self.w_[0] += self.eta * errors.sum()
            cost = (errors ** 2).sum() / 2.0 #J(W)
            self.cost_.append(cost)
            content=[]
            t=[]
            t.append(i+1)
            t.append(cost)
            content.append(t)
            content.append(self.w_.tolist())
            mesg=json.dumps(content)
            websocket.send_message(mesg)  #使用第三方平台(websocket技术),实时数据传递到前端
            time.sleep(1.5)
        # print output
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, X):
        return self.net_input(X)

    def predict(self, X):
        return np.where(self.activation(X) >= 0, 1, -1 )


#训练神经网络，并将训练得到的参数保存到csv文件中
def train(eta,n):
    #获取训练数据资源
    df = pd.read_csv('weather_data.csv', header=None)
    y = df.loc[0:100,6].values
    X = df.loc[0:100,[0,1,2,3,4,5]].values #取训练数据源的0-100行数据，每行取第0-5列的数据
    ada = weather_neaural(eta=eta, n_iter=n,w_flag=0)
    ada.fit(X, y)
    # print y
    #保存训练好的参数W
    with open("weather_w.csv", "wb+") as fw:
        writer = csv.writer(fw)
        writer.writerow(ada.w_)
    # #画图
    # page=pyecharts.Page()
    # #代价曲线图
    # line =pyecharts.Line("差距J(w)")
    # attr=np.arange(ada.n_iter)
    # line.add("差距J(w)", attr, ada.cost_, is_fill=True, line_opacity=0.2, area_opacity=0.4, symbol=None)
    # page.add(line)
    # page.render()
    # # webbrowser.open("http://localhost:63342/aproject/render.html")


# train(0.0001,40000)
#
# aobj=weather_neaural(eta=0.0001, n_iter=100,w_flag=1)
# df = pd.read_csv('weather_data.csv', header=None)
# y = df.loc[0:100,6].values
# X = df.loc[0:100,[0,1,2,3,4,5]].values #取训练数据源的0-100行数据，每行取第0-5列的数据
# print type(X)
# # print '预判结果：',
# # print aobj.predict(X)
# # print '实际结果：',
# # print y

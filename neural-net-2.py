#"coding=utf-8"
'''
自适应神经网络demo
'''
import numpy as np
import pandas as pd
import sys
import csv
reload(sys)
sys.setdefaultencoding('utf-8') #编码问题,将读取外部文件默认为utf-8
class AdalineGD(object):
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

    def __init__(self, eta=0.01, n_iter=50):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        """
        X:shape,二维数组[n_samples, n_features]
        example: x:[[1,2,3],[4,5,6]]===>x:shape:[2,3]
        n_samples 表示X中含有训练数据条目数
        n_features 含有4个数据的一维向量，用于表示一条训练数目

        y:一维向量
        用于存储每一训练条目对应的正确分类
        """
        self.w_ = np.zeros(1 + X.shape[1])
        self.cost_ = []
        """
        注意自在训练神经网络的时候，一次迭代就将取到的所有数据输入，往复输入，往复调整
        """
        for i in range(self.n_iter):
            # print '第%s次训练，w参数为：'%(i),
            # print self.w_[0]
            output = self.net_input(X)
            errors = (y - output)
            # print '，errors：',
            # print errors
            self.w_[1:] += self.eta * X.T.dot(errors)  #X.T 转秩 ;dot,矩阵相乘
            self.w_[0] += self.eta * errors.sum()
            # print errors.sum()
            cost = (errors ** 2).sum() / 2.0 #J(W)
            # self.cost_.append(cost)
            # print '第%s次训练，w参数为：'%(i),
            # print self.w_
            # print '代价：',
            # print cost
        # print output,
        # print len(output)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, X):
        return self.net_input(X)

    def predict(self, X):
        return np.where(self.activation(X) >= 0, 1, -1 )


#获取训练数据资源
df = pd.read_csv('iris.data.csv', header=None)
# print df.loc[0:0].values[0]
y = df.loc[0:100, 4].values
y = np.where( y == 'Iris-setosa', -1, 1) #数据处理，处理完毕后传入模型
X = df.loc[0:100, [0, 2]].values #取训练数据源的0-100行数据，每行取第0、2列的数据
# print y,
# print len(y)
ada = AdalineGD(eta=0.0001, n_iter=2)
ada.fit(X, y)
# with open("weather_w.csv", "a") as fw:
#     writer = csv.writer(fw)
#     writer.writerow(ada.w_)
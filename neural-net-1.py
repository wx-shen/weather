#"coding=utf-8"
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import sys
reload(sys)
sys.setdefaultencoding('utf-8') #编码问题,将读取外部文件默认为utf-8
class Perceptron(object):

    def __init__(self, eta = 0.01, n_iter = 10):
        self.eta = eta         #学习率，（0-1之间的小数）
        self.n_iter = n_iter   #n_iter:权重向量的训练次数
        pass

    def fit(self, X, y):
        '''
        输入训练数据， 培训神经元， X输入样本向量， y对应样本分类
        X:shape[n_samples, n_features]
        X:[[1, 2, 3], [4, 5, 6]]
        n_samples:2
        n_features:3
        y:[1, -1]
        '''

        """
        初始化权重向量为0
        加1是因为前面算法提到的w0, 也就是步调函数阈值，其实也就是偏置
        """
        self.w_ = np.zeros(1 + X.shape[1]) #w_:神经分叉权重向量

        self.errors_ = []
        for _ in range(self.n_iter):
            errors = 0    #用于记录神经元判断出错次数
            for xi, target in zip(X, y):  #zip:[[1,2],[3,4]],[5,6]=>[[1,2,5],[3,4,6]]

                #update = eta * (y - y')
                update = self.eta * (target - self.predict(xi))

                self.w_[1:] += update * xi    #xi 是一个向量
                self.w_[0] += update

                errors += int(update != 0.0)
                self.errors_.append(errors)
                pass
            pass

    def net_input(self, X):
        """
        z = W0*1 + W1*X1 + W2*X2 + ... Wn*Xn
        """
        return np.dot(X, self.w_[1:]) + self.w_[0]
    pass

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)
    pass
    pass


df = pd.read_csv('iris.data.csv', header=None)
df.head(10)
y = df.loc[0:100, 4].values
y = np.where( y == 'Iris-setosa', -1, 1) #数据处理，处理完毕后传入模型

X = df.loc[0:100, [0, 2]].values #取训练数据源的0-100行数据，每行取第0、4列的数据

ppn = Perceptron(eta=0.1, n_iter=10) #初始化类，指定学习率0.1，权重向量的训练次数10
ppn.fit(X, y) #调用训练函数，数据源X

"""
错误次数绘图
"""
# plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
# plt.xlabel('Epochs')
# plt.ylabel('error_times')
# plt.show()

def plot_decision_regions(X, y, classifier, resolution=0.02):
    markers = ('s', 'x', 'o', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    x1_min, x1_max = X[:, 0].min(), X[:, 0].max()
    x2_min, x2_max = X[:, 1].min(), X[:, 1].max()

    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))

    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)

    Z = Z.reshape(xx1.shape)

    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for inx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y==cl, 0], y=X[y==cl, 1], alpha=0.8, c=cmap(inx),
                   marker=markers[inx], label=cl)

plot_decision_regions(X, y, ppn, resolution=0.02)
plt.xlabel('flower stem-length')
plt.ylabel('petal-length')
plt.legend(loc='upper left')
plt.show()


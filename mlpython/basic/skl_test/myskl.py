#coding=utf-8

from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import numpy as np

def test_01():
    #a = np.arange(9).reshape(3,-1)
    a = np.array([[1,1,1],[2,2,2]], dtype=float)
    print 'u=',a.mean()

    # 计算方差
    arr_var = np.var(a)
    print 'theta=',arr_var

    # 计算标准差
    arr_std = np.std(a, ddof=1)
    print arr_std

    # (x-u)/theta
    s = preprocessing.scale(a)
    print s

def test_02():
    data = [[0,0],[0,0],[1,1],[1,1]]
    scaler = StandardScaler()

    # 计算均值 & 方差
    #print scaler.fit(data)
    #print scaler.mean_, scaler.var_
    
    #
    #print scaler.transform([[2,2]])

    print scaler.fit_transform(data)
    print scaler.mean_, scaler.var_

if __name__ == '__main__':
    #test_01()
    test_02()
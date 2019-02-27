# coding=utf-8

from sklearn.model_selection import KFold
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import numpy as np


def test_01():
    #a = np.arange(9).reshape(3,-1)
    a = np.array([[1, 1, 1], [2, 2, 2]], dtype=float)
    print('u=', a.mean())

    # 计算方差
    arr_var = np.var(a)
    print('theta=', arr_var)

    # 计算标准差
    arr_std = np.std(a, ddof=1)
    print(arr_std)

    # (x-u)/theta
    s = preprocessing.scale(a)
    print(s)


def test_02():
    data = [[0, 0], [0, 0], [1, 1], [1, 1]]
    scaler = StandardScaler()

    # 计算均值 & 方差
    # print scaler.fit(data)
    # print scaler.mean_, scaler.var_

    #
    # print scaler.transform([[2,2]])

    print(scaler.fit_transform(data))
    print(scaler.mean_, scaler.var_)


def test_03():
    x = np.array([[11, 22], [33, 43], [57, 66], [37, 28]])
    y = np.array([1, 2, 3, 4])
    kf = KFold(n_splits=2, shuffle=False, random_state=0)
    print(kf.get_n_splits(x))
    for train_index, test_index in kf.split(x):
        print('train index:', train_index)
        print('test index:', test_index)

from sklearn.datasets import load_iris 
from sklearn.linear_model import LogisticRegression
def test_04():
    X, y = load_iris(return_X_y=True)
    print(type(X), X.shape)
    print(type(y), y.shape)
    clf = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial').fit(X, y)
    print(clf.predict(X[:2, :]))


import pandas as pd
def test_05():
    mydict = [{'a':1, 'b':2, 'c':3},
              {'a':11, 'b':22,'c':33},
              {'a':32, 'b':12, 'c':55}]

    df = pd.DataFrame(mydict)
    print(df)
    print('\n iloc columns:')
    print(df.iloc[0])

    print('\n iloc rows:')
    print(df.iloc[[0,1]])

    

if __name__ == '__main__':
    # test_01()
    # test_02()
    #test_03()
    #test_04()
    test_05()
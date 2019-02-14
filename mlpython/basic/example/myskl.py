#coding=utf-8

from sklearn import linear_model

def test_skl():
    reg = linear_model.LinearRegression()
    reg.fit([[0,0], [1,1], [2,2]],[0, 1, 2])
    print reg.coef_

if __name__ =='__main__':
    test_skl()

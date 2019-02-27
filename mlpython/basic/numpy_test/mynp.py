#coding = utf-8

import numpy as np


def test_01():
    a = np.array([1, 2, 3])
    b = np.tile(a, 4)
    print (b)
    c = np.array([[1, 2], [3, 4]])
    d = np.tile(c, 2)
    print (d)

    x = np.array([4, 1, 2, 3])
    r = np.argsort(x)
    print (type(r))


def test_02():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print (a)
    print ('axis=0(column):', a.sum(axis=0))
    print ('axis=1(row):', a.sum(axis=1))



if __name__ == '__main__':
    # test_01()
    test_02()

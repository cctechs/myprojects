#coding=utf-8

import numpy as np


def test_01():
    a = [3,2,4,7,4,8]
    print a
    b = sorted(a)
    print b
    print a

    dd = {1,2,3,4}
    for i in range(len(dd)):
        print i

def test_02():
    a = 0
    b = 1
    c = 2

    print('test{0} is {1} and {2}').format(b,a,c)

if __name__ == '__main__':
    #test_01()
    test_02()
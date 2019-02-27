#coding=utf-8

import numpy as np
import pandas as pd

def test_np():
    
    print '\nthis is numpy test:\n'

    a = np.arange(12).reshape(3,-1)
    print a

    # 跨行相加
    print a.sum(axis=0)

    # 跨列相加
    print a.sum(axis=1)

    print '\n'

def test_pd():
    print 'this is pandas test:'
    b = pd.DataFrame(np.arange(24).reshape(4,-1), columns=['A', 'B', 'C', 'D', 'E', 'F'])
    print b
    # 跨行相加
    print b.sum(axis=0)
    # 跨列相加
    print b.sum(axis=1)

    # 计算均值
    print b.mean(axis=0) # 跨行
    print b.mean(axis=1) # 跨列

def test_pd_01():
    d = {'col1':[1,3,5], 'col2':[2,4,6], 'col3':[11,2,3]}
    df = pd.DataFrame(data=d)
    print df
    df = df.drop('col1', axis=1)
    print df

if __name__ == '__main__':
    test_np()
    test_pd()
    test_pd_01()
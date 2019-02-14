#coding=utf-8

import numpy as np 
import pandas as pd


def test_01():
    s = pd.Series([1,3,5, np.nan, 6, 8])
    #print s 
    dates = pd.date_range('20130101', periods=6)
    print dates

    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('abcd'))
    #print df
    print '\n=================================='
    d = {'col1':[1,2,3], 'col2':['b', 'c', 'k']}
    d1 = pd.DataFrame(d, index=['c1', 'c2', 'c3'])
    print d1

    print '\n=================================='
    df2 = pd.DataFrame(np.array([[-11,7,8],[5,25,6]]), index=['row1', 'row2'], columns=['p1', 'p2', 'p3'])
    print 'df2:\n', df2
    print '\nabs(df2):\n',abs(df2)
    
    print '\ndf2.T:\n',df2.T

    print type(df2)
    df3 = np.dot(df2.T, df2)
    print '\n:', df3
    
    print '\ndf2:\n', df2
    print '\nloc:\n', df2.loc['row1']
    #print '\naaa:\n', df2%2==0
    print '\nbefore df2:\n', df2
    df2.loc[:, 'p2']=29
    print '\nafter set value1:\n',df2 

    df2.loc['row1',:] = 40
    print '\nafter set value2:\n',df2 
    
    print '\ndf2[\'p2\']:\n', df2['p1']
    
    print '\ndf2[\'row1\']:\n', df2.loc['row1']
    print '\ndf2:\n', df2
    df2.loc[df2['p2']>35]=-98
    print '\nreset value:\n', df2
    print '\nabs():\n', df2.abs()
    








if __name__ == '__main__':
    test_01()

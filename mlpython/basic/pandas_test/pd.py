# coding=utf-8
import pandas as pd
import numpy as np


def test_01():
    a = pd.read_csv('food_info.csv')
    #print a
    #print (type(a))
    #print (help(pandas.read_csv))
    print a.head(3)
    print a.tail(4)
    print a.columns


def test_02():
    a = pd.read_csv('food_info.csv')
    col_names = a.columns.tolist()
    #print col_names
    print a.shape
    for c in col_names:
        if c.endswith('(g)'):
            print c


def test_03():
    data = pd.read_csv('titanic_train.csv')
    print data.head()
    #print data.columns
    age = data['Age']
    #print age.loc[0:10]
    age_is_null = pd.isnull(age)
    #print age_is_null

    # 统计确实值
    age_null_true = age[age_is_null]
    age_null_count = len(age_null_true)
    print age_null_count

    # 缺失值处理
    mean_age = sum(data['Age'])/len(data['Age'])
    print mean_age

    good_age = data['Age'][age_is_null == False]
    correct_mean_age = sum(good_age)/len(good_age)
    print correct_mean_age

    print data['Age'].mean()

    passs= data.pivot_table(index='Pclass', values='Survived', aggfunc=np.mean)
    print passs

    pas11= data.pivot_table(index='Pclass', values='Survived', aggfunc=np.sum)
    print pas11

    aaa = data.apply(myfunc)
    print aaa


def myfunc(column):
    item = column.loc[100]
    return item


if __name__ == '__main__':
    # test_01()
    # test_02()
    test_03()

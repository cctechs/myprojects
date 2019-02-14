#coding=utf-8

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def test_01():
    data = pd.read_csv('unrate.csv')
    data['DATE'] = pd.to_datetime(data['DATE'])
    print data.head(10)

    value = data[0:12]
    plt.plot(value['DATE'], value['VALUE'])
    plt.xticks(rotation=45)
    plt.xlabel('Month')
    plt.ylabel('UnEmplot Rate')
    plt.title('Monthly Trends')
    plt.show()

def test_02():
    fig = plt.figure()
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)
    plt.show()
    pass

def test_03():
    fig = plt.figure(figsize=(10,6))
    ax1 = fig.add_subplot(2,1,1)
    ax1.plot(np.random.random_sample(1,5,5), np.arange(5))

    ax2 = fig.add_subplot(2,1,2)
    plt.show()
    pass

if __name__ == '__main__':
    #test_01()
    #test_02()
    test_03()


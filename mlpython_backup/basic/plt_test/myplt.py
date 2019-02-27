# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt

def test_01():
    np.random.seed(19680801)
    x = np.arange(0.0, 50.0, 2.0)
    y = x**1.3+np.random.rand(*x.shape)*30
    s = np.random.rand(*x.shape)*800+500
    plt.scatter(x, y, s, c='g', marker=r'$\clubsuit$', alpha=0.5, label='Luck')
    plt.xlabel('Led')
    plt.ylabel('Gold')
    plt.legend(loc='upper left')
    plt.show()

if __name__ == '__main__':
    test_01()
    
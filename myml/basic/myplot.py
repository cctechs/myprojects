# coding=utf-8


import matplotlib.pyplot as plt
import numpy as np

##
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.ylabel('some numbers')
plt.show()

##
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--',
         t, t ** 2, 'bs',
         t, t ** 3, 'g^')
plt.grid(True)
plt.axis([0., 3., 0., 5.])
plt.text(1, 1, r'$\mu=100$')
plt.show()

##
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}

data['b'] = data['a'] + 10 * np.random.randn(50)

data['d'] = np.abs(data['d']) * 100

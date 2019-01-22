# coding=utf-8

import numpy as np

a = np.arange(15).reshape(3, 5)
print a
print a.shape
print a.ndim
print a.dtype.name
print a.itemsize
print a.size

a = np.array([2, 3, 4])
b = np.array([4, 5, 6])

items = list((5, 6, 7, 8, 9))

p = np.array(items)
print p

print np.add(a, b)

print (np.arange(10, 30, 5))
print (np.arange(10, 30, 5)).reshape(2, 2)

c = np.array([[1, 2], [3, 4]])
print c

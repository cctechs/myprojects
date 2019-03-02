# coding=utf-8

import numpy as np

a = np.array([1, 2, 3])
print(type(a))
print(a)


c = [1, 2, 3]
print(type(c))

d = (1, 2, 3)
print(type(d))

e = {}
print(type(e))


print(np.array([1, 2, 3]))
print(np.array([[1, 2, 3]]))

print(np.array([[1, 2, 3], [4, 5, 6]]))

print(np.ndarray(np.shape(2), buffer=np.array([1, 2]),
                 offset=np.int_().itemsize, dtype=int))

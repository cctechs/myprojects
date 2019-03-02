# coding=utf-8

from itertools import groupby
import itertools


nums = itertools.count()

for i in nums:
    if i > 10:
        break
    print(i)


cycle_strings = itertools.cycle('ABC')
i = 1
for str in cycle_strings:
    if i > 10:
        break
    print(str)
    i += 1


for k, v in groupby('aaabbcccaaccdd'):
    print(k, list(v))

print('\nzip\n')
a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8, 9]

zz = zip(a, b)
print(list(zz))
print(list(zip(a, c)))
print(list(zip(a, b, c)))
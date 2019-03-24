# coding=utf-8

from string import Template 

print(10//6)
print(10/6)

seq = ['one', 'two', 'three']

for elem in seq:
    print(elem)

for i, elem in enumerate(seq):
    print(i, elem)

print('a' in 'abc')
print('e' in 'abc')

print('*'*50)

s = Template('there are ${num} dogs')
print (s.substitute(num=3))

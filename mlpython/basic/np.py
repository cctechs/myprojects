# coding=utf-8
import numpy as np


def myfun(a):
    a = a + 1
    print (a)


def test_01():
    print('hello')
    myfun(9)
    a = np.array([2, 3, 4, 5, 6.0])  # same datatype
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    txt = np.genfromtxt("test.txt")


def test_02():
    vector = np.array([[1, 2, 3, 4, 5],[1,2,3,1,1]])
    print(vector == 2)
    print (vector.astype(float))
    print (vector.sum())
    print (vector.sum(axis=1))
    print (vector.sum(axis=0))

def test_03():
    a = np.arange(20)
    print (a.reshape(4, 5))

def test_04():
    a = np.random.random((2,3))
    print(a)

    print np.linspace(0, 2*np.pi, 10)

def test_05():
    a = np.floor(10*np.random.random((3, 4)))
    print a
    print (a.ravel())
    a = a.reshape(6,-1)
    print a
    print a.T

def test_06():
    a = np.floor(10*np.random.random((2,2)))
    b = np.floor(10*np.random.random((2,2)))
    print (a)
    print (b)
    #print (np.hstack((a, b)))
    c = np.hstack((a, b))
    print c
    # print (np.vstack((a, b)))
    d = np.vsplit(c, 2)
    print d

    e = np.hsplit(c, (0, 1))
    print e

# copy data
def test_07():
    a = np.arange(12)
    b = a
    print (id(a))
    print (id(b))
    print (a)
    c = a.view() # 浅拷贝，虽然指向不同的地址，但是元素值是共用的
    c[0] = 1234
    print c
    print a
    print (c is a)
    print (id(c))
    d = a.copy() # 深拷贝
    d[0] = 345
    print d
    print a

def test_08():
    data = np.sin(np.arange(20)).reshape(5,4)
    print data
    ind = data.argmax(axis = 0)
    print (ind)
    data_max = data[ind, range(data.shape[1])]
    print data_max

def test_09():
    a = np.arange(0, 40, 10)
    print a
    b = np.tile(a, (3, 5))
    print b

if __name__ == '__main__':
    #test_01()
    #test_02()
    #test_03()
    #test_04()
    #test_05()
    #test_06()
    #test_07()
    #test_08()
    test_09()
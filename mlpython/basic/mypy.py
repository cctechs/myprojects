#coding=utf-8

class BaseClass:
    __pwd = 'this is privated'
    _account = 'this is protected'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print 'BaseCalss:', self.name, self.age

class DriveClass(BaseClass):
    def show(self):
        print 'DriveCalss:', self.name, self.age
        print self.__doc__
        print self.__class__
        print self._account

def test_class():
    d = DriveClass('name', 'age')
    d.show()
    del d

class MyClass:
    x = 5
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.myfunc()
    
    def myfunc(self):
        print 'this is a test'

def my_list():
    list1 = ['123', '456', 'qwe']
    print list1


def test_01():
    print 'hello'
    my_function(p2='qwe')
    p1 = MyClass('weber',23)
    print p1.x, p1.age, p1.name
    my_list()

    # 列表
    l1 = []
    l1.append('zzzgoogle')
    l1.append('hello')
    l1.append('world')
    print 'this is l1:',l1
    del l1[1]
    print 'after del:',l1
    print 'max:', max(l1)
    # 元组
    print '\n========================================='
    tup1 =  ('aaa', 'ccc', 'bbb')
    print 'tup1:', tup1
    tup2 = (50,)
    print 'tup2:',tup2
    #del tup2
    #print 'after del:', tup2
    print 'len(tup1):', len(tup1)
    print '\n========================================='
    dict = {}
    dict['name'] = 'weber'
    print dict
    print dict['name']
    print dict['123']

    print '\n\n\n\n'

def my_function(p1='001', p2='002', p3='003'):
    print p1
    print p2
    print p3

if __name__ == "__main__":
    #test_01()
    test_class()
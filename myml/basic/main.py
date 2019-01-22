# coding=utf-8

def moving_average(a, w=10):
    if len(a) <= w:
        print 'here'
        return a[:]
    return [v if k < w else sum(a[(k - w):k]) / w for k, v in enumerate(a)]
    #return [v if k < w else sum(a[k - w:k])/w for k, v in enumerate(a)]


def moving_average2(a, w=10):
    if len(a) < w:
        return a[:]
    ret = []
    for idx, val in enumerate(a):
        if idx < w:
            ret.append(val)
        else:
            ret.append(sum(a[(idx - w):idx]) / w)
    return ret[:]


if __name__ == '__main__':
    a = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    k1 = moving_average(a, 3)
    k2 = moving_average2(a, 3)
    print (k1)
    print (k2)

    pass

    add = lambda x, y, z: x + y + z
    print (add(1, 2, 3))

    squared = []
    for x in range(10):
        squared.append(x ** 2)

    print (squared)

    xx = [i for i in range(30) if i % 3 is 0]
    print (xx)

    mcase = {'a': '1', 'B': '2'}
    for k in mcase.keys():
        print k

    print mcase
    mcase = {v: k for k, v in mcase.items()}
    for k, v in mcase.items():
        print k, v
    print mcase

    names = ['A', 'B', 'C']
    names = [k.lower() + '1' for k in names]
    print (names)

    items = [1, 2, 3, 4, 5]

    squared = list(map(lambda x: x ** 2, items))
    print(squared)

    items = list((1, 2, 3, 4, 5, 6, 7))
    print items

    ttt = list("hello")
    print ttt

    str1 = 'hello %s' % 'world'
    print str1

    t1 = tuple([1, 2, 3])
    print t1

    t1 = list((1, 2, 3))
    print t1

    a = list((1, 2, 3))
    a[0] = 2
    print a

    b = tuple([1, 2, 3])
    # b[0] = 2
    print b

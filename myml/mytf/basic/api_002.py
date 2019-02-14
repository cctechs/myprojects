# coding=utf-8

import tensorflow as tf

w = tf.Variable(1.3)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    #####################################
    # 字符串转换为数字
    print (sess.run(tf.string_to_number('134', tf.int32)))

    #
    print (sess.run(tf.to_double(123)))

    # 转换为指定类型
    print (sess.run(tf.cast(w, tf.int32)))

    #####################################
    # 按指定类型与形状生成值为1的张量
    print (sess.run(tf.ones([2, 3], tf.int32)))

    # 按指定类型与形状生成值为0的张量
    print (sess.run(tf.zeros([4, 5], tf.int32)))

    # 生成 和输入张量一样形状与类型的1
    tensor = [[1, 2, 3], [4, 5, 6]]
    print (sess.run(tf.ones_like(tensor)))

    print (sess.run(tf.zeros_like(tensor)))

    # 为指定形状填值
    print (sess.run(tf.fill([2, 3], 9)))

    # 生成常量
    print (sess.run(tf.constant([2, 3], 1)))

    # 规约函数
    x = [[1, 1, 1], [1, 1, 1]]
    print (sess.run(tf.reduce_sum(x)))

    print ('-----------------')
    x = [[6, 3, 5], [4, 8, 9]]
    print (sess.run(tf.reduce_min(x)))
    print (sess.run(tf.reduce_max(x)))
    print (sess.run(tf.reduce_mean(x)))
    print (sess.run(tf.reduce_prod(x, 0)))
    x = [[True, True], [True, False]]
    print (sess.run(tf.reduce_all(x, 0)))
    print (sess.run(tf.reduce_any(x, 0)))

    print ('-----------------')
    x = [[2, 3, 5], [4, 9, 9]]
    y = [[1,2,3], [4,5,6]]
    print (sess.run(tf.argmin(x)))
    print (sess.run(tf.argmin(x, 0)))
    print (sess.run(tf.argmin(x, 1)))


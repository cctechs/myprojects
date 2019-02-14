# coding=utf-8

import tensorflow as tf

a = tf.Variable(tf.ones([3, 5]), name='123')
matrix1 = tf.constant([[3, 3, 3]])
matrix2 = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

c = tf.constant(1)
product = tf.matmul(matrix1, matrix2)

one = tf.constant(1)
oldstate = tf.Variable(0, name='counter')
new_value = tf.add(oldstate, one)
update = tf.assign(oldstate, new_value)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    devices = sess.list_devices()
    for d in devices:
        print (d.name)

    print (sess.run(a))
    print (sess.run(matrix1))
    print (sess.run(matrix2))
    print (sess.run(product))
    print (sess.run(c))

    print (sess.run(tf.add(matrix2, matrix2)))

    for _ in range(3):
        sess.run(update)
        print (sess.run(oldstate))

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)

params = tf.placeholder(tf.float32)
fnFig = tf.nn.sigmoid(params)

W = tf.Variable(tf.random_normal([1, 5]), name='weight')

with tf.Session() as sess:
    # for k in range(10):
    #    print (sess.run(output, feed_dict={input1: [[k, k], [k, k]], input2: [[k, k], [k, k]]}))

    # 激活函数

    sess.run(tf.global_variables_initializer())
    print ('here')
    print(sess.run(fnFig, feed_dict={params: 0}))

    print(sess.run(W))

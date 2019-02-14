# coding=utf-8


import tensorflow as tf

a = tf.constant(3)
b = tf.constant(4)

c = tf.placeholder(tf.int16)
d = tf.placeholder(tf.int16)

add = tf.add(c, d)

f = tf.Variable(tf.zeros([2, 3, 5]), name='bias')

f2 = tf.Variable(tf.ones([1, 2, 3, 4, 5]))

saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print sess.run(f)
    print sess.run(f2)
    print(sess.run(a + b))
    print(sess.run(a * b))
    print(sess.run(add, feed_dict={c: 2, d: 4}))
    saver.save(sess, './123')

# coding=utf-8

import tensorflow as tf

print(tf.__version__)

w = tf.Variable([[0.5, 1.0]])
x = tf.Variable([[2.0], [1.0]])

y = tf.matmul(w, x)

init_opt = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init_opt)
    print(y.eval())
    print(type(y))

# coding=utf-8

import tensorflow as tf
import pylab
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)
tf.reset_default_graph()
x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

W = tf.Variable(tf.random_normal([784, 10]))
b = tf.Variable(tf.zeros([10]))

pred = tf.nn.softmax(tf.matmul(x, W) + b)

saver = tf.train.Saver()

model_path = 'log/521model.ckpt'

with tf.Session() as sess:

    # 初始化变量
    sess.run(tf.global_variables_initializer())

    # 恢复模型变量
    saver.restore(sess, model_path)

    # 计算准确率
    current_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    print (current_prediction)

    accuracy = tf.reduce_mean(tf.cast(current_prediction, tf.float32))

    print ('accuracy:', accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))

    output = tf.argmax(pred, 1)

    batch_x, batch_y = mnist.train.next_batch(2)
    print (batch_x, batch_y)

    print (output, pred)

    outputval, predv = sess.run([output, pred], feed_dict={x: batch_x})

    print(outputval, predv, batch_y)

    im = batch_x[0]
    im = im.reshape(-1, 28)

    pylab.imshow(im)
    pylab.show()

    im = batch_x[1]
    im = im.reshape(-1, 28)
    pylab.imshow(im)
    pylab.show()

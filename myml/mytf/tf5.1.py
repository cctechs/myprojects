# coding=utf-8

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import pylab

mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

print (mnist.train.images)
print (mnist.train.images.shape)

im = mnist.train.images[1]
im = im.reshape(-1, 28)
pylab.imshow(im)
pylab.show()

# 测试训练集
print (mnist.test.images.shape)

tf.reset_default_graph()
x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

W = tf.Variable(tf.random_normal([784, 10]))
b = tf.Variable(tf.zeros([10]))

pred = tf.nn.softmax(tf.matmul(x, W) + b)

cost = tf.reduce_mean(-tf.reduce_sum(y * tf.log(pred), reduction_indices=1))

learning_rate = 0.01

# 梯度下降算法
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# 训练次数
training_epochs = 25

batch_size = 100

display_step = 1

saver = tf.train.Saver()

with tf.Session() as sess:
    # 初始化变量
    sess.run(tf.global_variables_initializer())

    for epoch in range(training_epochs):
        avg_cost = 0
        total_batch = int(mnist.train.num_examples / batch_size)
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            _, c = sess.run([optimizer, cost], feed_dict={x: batch_xs, y: batch_ys})
            avg_cost += c / total_batch

        if (epoch + 1) % display_step == 0:
            print ('epoch:', '%04d' % (epoch + 1), 'cost:', '{:.9f}'.format(avg_cost))

    print ('finished')

    # 测试model
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print ('Accurracy', accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))

    model_path = 'log/521model.ckpt'
    save_path = saver.save(sess, model_path)
    print ('Model saved in file:%s' % save_path)

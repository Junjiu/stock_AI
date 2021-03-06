import tensorflow as tf
import numpy as np
from Predicter import Predicter
from Data_reader import Data_reader

class Builder_Softmax:
    x = tf.placeholder("float", [None, 49], name='x1')  # placeholder是一个占位符，None表示此张量的第一个维度可以是任何长度的
    y = tf.placeholder("float", [None, 200], name='y1')
    w = tf.Variable(tf.zeros([49, 200]), name="w")  # 定义w维度是:[784,10],初始值是0
    b = tf.Variable(tf.zeros([200])+0.1)  # 定义b维度是:[10],初始值是0
    y_ = tf.nn.softmax(tf.matmul(x, w) + b,name="output")
    cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=y_)

    # 梯度下降
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)
    # 初始化
    init = tf.global_variables_initializer()
    def train(self):
        reader = Data_reader()
        features, result,number= reader.read(50, 200, "train")
        sess = tf.Session()
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord, sess=sess)
        sess.run(self.init)
        for i in range(3000):
            #print(sess.run(self.w))
            example, label = sess.run([features, result])
            example = np.reshape(example, (1, 49))
            label = np.reshape(label, (1, 200))
            sess.run(self.train_step, feed_dict={self.x: example, self.y: label})
            # print("Do training for %dth data" % i)
            # print(sess.run(self.cross_entropy,feed_dict={self.x: example, self.y: label}))
            # print(label)

        # print(sess.run(self.w))
        saver = tf.train.Saver()
        save_path = saver.save(sess, "D:/model/model.ckpt")
        print("Model saved in file: %s" % save_path)
        coord.request_stop()
        coord.join(threads)
        sess.close()

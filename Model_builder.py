import tensorflow as tf
import numpy as np
from Predicter import Predicter
from Data_reader import Data_reader

class A:
    def train(self):
        reader = Data_reader()
        features, result = reader.read(50, 200, "train")
        sess = tf.Session()
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord, sess=sess)
        # ==========================================================
        # build model
        x = tf.placeholder("float", [None, 49], name='x1')  # placeholder是一个占位符，None表示此张量的第一个维度可以是任何长度的

        w = tf.Variable(tf.zeros([49, 200]), name="w")  # 定义w维度是:[784,10],初始值是0
        b = tf.Variable(tf.zeros([200]))  # 定义b维度是:[10],初始值是0
        y = tf.matmul(x, w) + b
        # loss
        y_ = tf.nn.softmax(y, name="y")

        cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=y,
                                                                labels=y_)  # 用 tf.log 计算 y 的每个元素的对数。接下来，我们把 y_ 的每一个元素和 tf.log(y_) 的对应元素相乘。最后，用 tf.reduce_sum 计算张量的所有元素的总和。

        # 梯度下降
        train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
        # 初始化
        init = tf.global_variables_initializer()
        sess.run(init)
        # ===================================================================
        for i in range(300):
            print("Do training for %dth data" % i)
            example, label = sess.run([features, result])
            example = np.reshape(example, (1, 49))
            label = np.reshape(label, (1, 200))
            sess.run(train_step, feed_dict={x: example, y_: label})
        print(sess.run(w))
        saver = tf.train.Saver()
        save_path = saver.save(sess, "D:/model/model.ckpt")
        print("Model saved in file: %s" % save_path)
        coord.request_stop()
        coord.join(threads)
        sess.close()
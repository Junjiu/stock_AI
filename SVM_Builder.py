import tensorflow as tf
import numpy as np
from Predicter import Predicter
from Data_reader import Data_reader
class Builder_SVM:
    input_size=202
    output_size=1
    train_num=0
    x = tf.placeholder("float", [None, input_size], name='x1')  # placeholder是一个占位符，None表示此张量的第一个维度可以是任何长度的
    y = tf.placeholder("float", [None, 1], name='y1')
    w = tf.Variable(tf.ones([input_size, 1]), name="w")  # 定义w维度是:[784,10],初始值是0
    b = tf.Variable(tf.zeros([1]),name="b")  # 定义b维度是:[10],初始值是0
    # loss
    y_ = tf.add(tf.matmul(x, w),b,name="output")
    regularization_loss = tf.reduce_sum(tf.square(w))
    hinge_loss = tf.reduce_sum(tf.maximum(tf.zeros([input_size, 1]),
                                          1-y * y_));
    svm_loss = 230*regularization_loss+hinge_loss


    train_step = tf.train.GradientDescentOptimizer(0.001).minimize(svm_loss)

    # 初始化
    init = tf.global_variables_initializer()

    def train(self):
        reader = Data_reader()
        features, result = reader.read(self.input_size, 1, "train_kernel.csv")
        sess = tf.Session()
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord, sess=sess)
        sess.run(self.init)
        for i in range(200):
            self.train_num+=1
            example, label = sess.run([features, result])
            example = np.reshape(example, (1, self.input_size))
            label = np.reshape(label, (1, 1))
            sess.run(self.train_step, feed_dict={self.x: example, self.y:label})
            if i%30==0:
                print("Do training for %d th data" % self.train_num)
                print(sess.run(self.svm_loss, feed_dict={self.x: example, self.y: label}))
                print(sess.run(self.y_, feed_dict={self.x: example}))
                print(label)

        # print(sess.run(self.w))
        saver = tf.train.Saver()
        save_path = saver.save(sess, "D:/model/model.ckpt")
        print("Model saved in file: %s" % save_path)
        coord.request_stop()
        coord.join(threads)
        sess.close()
        print("SVM model trained finished")


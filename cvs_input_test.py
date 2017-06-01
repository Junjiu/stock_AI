#coding=utf-8

import tensorflow as tf
import numpy as np
from tensorflow.core.protobuf import saver_pb2
filename_queue = tf.train.string_input_producer(["D:/stock_data/train_current_data.csv"])

reader = tf.TextLineReader()
key, value = reader.read(filename_queue)

# Default values, in case of empty columns. Also specifies the type of the
# decoded result.
record_defaults = [[1.0]]*251
cols= tf.decode_csv(
    value, record_defaults=record_defaults)
features = tf.stack(cols[0:49])

result=tf.stack(cols[49:248])
sess = tf.Session()
# Start populating the filename queue.
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(coord=coord,sess=sess)
#==========================================================
x = tf.placeholder("float", [None, 49],name='x1')  # placeholder是一个占位符，None表示此张量的第一个维度可以是任何长度的
#
w = tf.Variable(tf.zeros([49, 199]),name="w")  # 定义w维度是:[784,10],初始值是0
b = tf.Variable(tf.zeros([199]))  # 定义b维度是:[10],初始值是0
y = tf.matmul(x,w) + b
# loss
y_ =  tf.nn.softmax(y,name="y")

cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=y,labels=y_)  # 用 tf.log 计算 y 的每个元素的对数。接下来，我们把 y_ 的每一个元素和 tf.log(y_) 的对应元素相乘。最后，用 tf.reduce_sum 计算张量的所有元素的总和。

  # 梯度下降
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
  # 初始化
init = tf.global_variables_initializer()

sess.run(init)

#=====================================================

for i in range(10):
  print("Do training for %dth data"%i)
  # Retrieve a single instance:
  example, label = sess.run([features, result])
  #print(example)
  #print(label)
  example=np.reshape(example,(1,49))
  label=np.reshape(label,(1,199))
  sess.run(train_step, feed_dict={x: example, y_: label})

print(sess.run(w))
# example = np.array([[0,1,3,0],[0,0,50,0]],dtype=int)
# label = np.array([[0,0,1],[0,1,0]],dtype=bool)
# correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
# accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
# print(sess.run(accuracy, feed_dict={x: example, y_: label}))
# print(sess.run(y_,feed_dict={x:example}))




saver = tf.train.Saver()

save_path = saver.save(sess, "D:/model/model.ckpt")
print("Model saved in file: %s" % save_path)
coord.request_stop()
coord.join(threads)
sess.close()

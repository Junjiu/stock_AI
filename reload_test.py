import tensorflow as tf
import  numpy as np
# Create some variables.
saver = tf.train.import_meta_graph('/model/model.ckpt.meta')
# Add ops to save and restore all the variables.
saver = tf.train.Saver()

# Later, launch the model, use the saver to restore variables from disk, and
# do some work with the model.
with tf.Session() as sess:
  # Restore variables from disk.
  saver.restore(sess, "/model/model.ckpt")
  print("Model restored.")
  print(sess.run("w:0"))


  # Default values, in case of empty columns. Also specifies the type of the
  # decoded result.


# y=tf.matmul(x,w)+b
# sess.run(tf.global_variables_initializer())
# #output=tf.convert_to_tensor(output,dtype=tf.float32)
# print (sess.run(y,feed_dict))
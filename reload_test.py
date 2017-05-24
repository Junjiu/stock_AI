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
  #print(sess.run("w:0"))

  filename_queue = tf.train.string_input_producer(["D:/stock_data/test_data.csv"])

  reader = tf.TextLineReader()
  key, value = reader.read(filename_queue)

  # Default values, in case of empty columns. Also specifies the type of the
  # decoded result.
  record_defaults = [[1.0]] * 249
  cols = tf.decode_csv(
    value, record_defaults=record_defaults)
  features = tf.stack(cols[0:49])
  result = tf.stack(cols[49:248])
  coord = tf.train.Coordinator()
  threads = tf.train.start_queue_runners(coord=coord, sess=sess)
  f = open("D:/stock_data/predict_result.csv", "w+")
  for i in range(3500):
    example = sess.run(features)
    label=sess.run(result)
    example = np.reshape(example, (1, 49))
    label = np.reshape(label, (1, 199))
    feed_dict = {tf.get_default_graph().get_tensor_by_name(name='x1:0'): example}
    re = sess.run(tf.get_default_graph().get_tensor_by_name(name='y:0'), feed_dict)
    weight = 0
    sum = 0
    j=0
    max=re[0][0]
    for i in range(0, len(re[0])):
      weight += re[0][i] * (i - 99)
      sum += re[0][i]

      if max<re[0][i]:
        max=re[0][i]
        j=i


    delta = weight / sum
    f.write(str(j))
    f.write("\n")
  f.close()

# y=tf.matmul(x,w)+b
# sess.run(tf.global_variables_initializer())
# #output=tf.convert_to_tensor(output,dtype=tf.float32)
# print (sess.run(y,feed_dict))
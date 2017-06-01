import  tensorflow as tf
import numpy as np
from Data_reader import  Data_reader
class Predicter:

    def predict(self,num):
        with tf.Session() as sess:
            saver = tf.train.Saver()
            saver.restore(sess, "/model/model.ckpt")
            reader = Data_reader()
            features, result ,number= reader.read(50, 200, "test")
            coord = tf.train.Coordinator()
            threads = tf.train.start_queue_runners(coord=coord, sess=sess)
            f = open("D:/stock_data/predict_result.csv", "w+")
            for j in range(num):
                example,label=sess.run([features,result])
                example = np.reshape(example, (1, 49))
                label = np.reshape(label, (1, 200))
                feed_dict = {tf.get_default_graph().get_tensor_by_name(name='x1:0'): example}
                re = sess.run(tf.get_default_graph().get_tensor_by_name(name='y:0'), feed_dict)
                j = 0
                max = re[0][0]
                for i in range(0, len(re[0])):
                    if max < re[0][i]:
                        max = re[0][i]
                        j = i
                f.write(str(int(sess.run(number)))+"  "+str(j))
                f.write("\n")
            f.close()
            coord.request_stop()
            coord.join(threads)
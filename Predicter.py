import  tensorflow as tf
import numpy as np
from Data_reader import  Data_reader
class Predicter:
    right_sum=0
    wrong_sum=0
    def predict_svm(self,num=200):
        self.predict(num,202,1)
    def predict_softmax(self,num):
        self.predict(num,50,200)
    def predict(self,num,e_num,l_num):
        right = 0
        wrong = 0
        with tf.Session() as sess:
            print("load model")
            saver = tf.train.Saver()
            saver.restore(sess, "/model/model.ckpt")
            # print("w:")
            # print(sess.run(tf.get_default_graph().get_tensor_by_name("w:0")))
            reader = Data_reader()
            features, result= reader.read(e_num, l_num, "pre_kernel.csv")
            coord = tf.train.Coordinator()
            threads = tf.train.start_queue_runners(coord=coord, sess=sess)
            f = open("D:/stock_data/final_result.csv", "w+")
            for j in range(num):
                example,label=sess.run([features,result])
                example = np.reshape(example, (1, e_num))
                label = np.reshape(label, (1, l_num))
                feed_dict = {tf.get_default_graph().get_tensor_by_name(name='x1:0'): example}
                re = sess.run(tf.get_default_graph().get_tensor_by_name(name='output:0'), feed_dict)
                if(re[0][0]<=-1 and label[0][0]==-1) or (re[0][0]>=1 and label[0][0]==1):
                    right+=1
                if (re[0][0] <= -1 and label[0][0] == 1) or (re[0][0] >= 1 and label[0][0] == -1):
                    wrong+=1
                # print(re[0][0])
                # print(label[0][0])
                f.write(str(re[0][0]))
                f.write("\n")
            print(right)
            print(wrong)
            self.right_sum+=right
            self.wrong_sum+=wrong
            f.write(str(right)+"\n")
            f.write(str(wrong) + "\n")
            f.write("=================="+"\n")
            f.close()
            coord.request_stop()
            coord.join(threads)

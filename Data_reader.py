import  tensorflow as tf
class Data_reader:
    def read(self,exam_len,re_len,style):
        # in this svm ,the exam_len should be 52  , re_len should be 1
        filename_queue = tf.train.string_input_producer(["D:/stock_data2.0/%s"%style])
        reader = tf.TextLineReader()
        key, value = reader.read(filename_queue)
        record_defaults = [[1.0]] * (exam_len+re_len+1)
        cols = tf.decode_csv(
            value, record_defaults=record_defaults)
        features = tf.stack(cols[0:exam_len])
        result = tf.stack(cols[exam_len:exam_len+re_len])
        return features,result
import  tensorflow as tf
class Data_reader:
    def read(self,exam_len,re_len,style):
        # in this case ,the exam_len should be 50  , re_len should be 200
        filename_queue = tf.train.string_input_producer(["D:/stock_data/%s_current_data.csv"%style])
        reader = tf.TextLineReader()
        key, value = reader.read(filename_queue)
        record_defaults = [[1.0]] * (exam_len+re_len+1)
        cols = tf.decode_csv(
            value, record_defaults=record_defaults)
        features = tf.stack(cols[1:exam_len])

        result = tf.stack(cols[exam_len:exam_len+re_len])
        return features,result
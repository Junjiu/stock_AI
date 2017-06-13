# from Softmax_Builder import  Builder_Softmax
from SVM_Builder import Builder_SVM
from Predicter import Predicter
from Build_data import  Pirce
class Stock_AI:

    # builder_svm=Builder_SVM()
    # # builder_softmax=Builder_Softmax()
    predicter=Predicter()
    price=Pirce()

    def run(self):
        self.price.build_data("train")
        self.price.build_data("pre")
        for i in range(1):
            print("start runing")
            builder_svm = Builder_SVM()
            for j in range(3,6):
                self.price.build_kernal(j)
                builder_svm.train()
                self.predicter.predict_svm()
                print("right_sum")
                print(self.predicter.right_sum)
                print("wrong_sum")
                print(self.predicter.wrong_sum)
                print("accuracy")
                print(self.predicter.right_sum/(self.predicter.wrong_sum+self.predicter.right_sum))
            self.predicter.wrong_sum = 0
            self.predicter.right_sum = 0
            for j in range(10):
                self.price.build_kernal(j)
                self.predicter.predict_svm()
                print("======================")
                print("right_sum")
                print(self.predicter.right_sum)
                print("wrong_sum")
                print(self.predicter.wrong_sum)
                print("accuracy")
                accuracy=self.predicter.right_sum / (self.predicter.wrong_sum + self.predicter.right_sum)
                print(accuracy)
                f_flag=open("D:/stock_data2.0/flag1.csv","r+")
                f_flag.write(str(i)+"  :"+str(accuracy))
                f_flag.close()



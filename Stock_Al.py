from  Data_getter import Data_getter
from Model_builder import  Builder
import os
from Predicter import Predicter
from Tester import Tester
class Stock_AI:

    getter = Data_getter()
    builder=Builder()
    predicter=Predicter()
    tester=Tester()

    def run(self):
        # self.getter.get_data()
        f_total=open("D:/stock_data/total_output.csv","w+")
        f_pre = open("D:/stock_data/pre_output.csv","w+")
        interest=0
        total=0

        for i in range(39,20,-1):
            print("%dth test:"%i)
            self.getter.build_data(i)
            self.builder.train()
            self.predicter.predict(300)
            t,p=self.tester.test()
            interest+=p
            total+=t
            f_total.write(str(t)+"\n")
            f_pre.write(str(p)+"\n")

        print("interest :"+str(interest))
        print("total :"+str(total))
        f_total.close()
        f_pre.close()
from  Data_getter import Data_getter
import Model_builder
import os
from Predicter import Predicter
from Tester import Tester
class Stock_AI:

    getter = Data_getter()

    predicter=Predicter()
    tester=Tester()
    def run(self):
        #self.getter.get_data()
        for i in range(1):
            print("%dth test:"%i)
            os.system("D:/tensorflow_test/Model_builder.py")
            self.predicter.predict(300)
            self.tester.test()


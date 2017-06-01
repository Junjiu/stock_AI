from  Data_getter import Data_getter


from Predicter import Predicter
from Tester import Tester
from  Model_builder import  A
a=A()
a.train()
getter=Data_getter()
predic=Predicter()

predic.predict(350)
# tester=Tester()
# t_list=[]
# p_list=[]
# for i in range(20):
#     print(i)
#     getter.build_test_data(i)
#     predic.predict(350)
#     total,predict=tester.test()
#     t_list.append(total)
#     p_list.append(predict)
# t_sum=0;
# p_sum=0;
# for i in range(len(t_list)):
#     print("Total: %f" % (t_list[i]*100))
#     print("Prediction: %f" % (p_list[i]*100))
#     t_sum+=t_list[i]*100
#     p_sum+=p_list[i]*100
# print("t_sum:  %f"%t_sum)
# print("p_sum:  %f"%p_sum)
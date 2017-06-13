#coding=utf-8
import math
import  numpy as np
class Pirce:
    def get_dic(self):
        price_dic = {}
        volume_dic = {}
        feedback_dic = {}
        f_price = open("D:/stock_data2.0/TRD_Dalyr.csv", encoding="utf-16")
        for line in f_price:
            line = line.split()
            if not line[0] in price_dic:
                price_dic[line[0]] = []
                volume_dic[line[0]] = []
                feedback_dic[line[0]] = []
            price_dic[line[0]].append(line[2])
            volume_dic[line[0]].append(line[3])
            feedback_dic[line[0]].append(line[4])
        quick_dic = {}
        cash_dic = {}
        f_pay = open("D:/stock_data2.0/FI_T1(pay).csv", encoding="utf-16")
        for line in f_pay:
            line = line.split()
            if not line[0] in quick_dic and line[2] == 'A':
                quick_dic[line[0]] = line[3]
                cash_dic[line[0]] = line[4]
        f_interes = open("D:/stock_data2.0/FI_T2(company interest).csv", encoding="utf-16")
        interest_dict = {}
        for line in f_interes:
            line = line.split()
            interest_dict[line[0]] = line[2]
        f_stru = open("D:/stock_data2.0/FI_T3(stucture).csv", encoding="utf-16")
        stru1 = {}
        stru2 = {}
        stru3 = {}
        for line in f_stru:
            line = line.split()
            if not line[0] in stru1 and line[2] == "A":
                stru1[line[0]] = line[3]
                stru2[line[0]] = line[4]
                stru3[line[0]] = line[5]
        f_store = open("D:/stock_data2.0/FI_T4（store).csv", encoding="utf-16")
        store_dic = {}
        for line in f_store:
            line = line.split()
            try:
                if not line[0] in store_dic:
                    store_dic[line[0]] = line[3]
            except:
                pass
        f_risk = open("D:/stock_data2.0/FI_T7(risk).csv", encoding="utf-16")
        risk_dic = {}
        for line in f_risk:
            line = line.split()
            if not line[0] in risk_dic and line[2] == "A":
                risk_dic[line[0]] = line[3]
        return price_dic, volume_dic,feedback_dic,quick_dic,cash_dic,interest_dict,stru1,stru2,stru3,risk_dic,store_dic
    def build_data(self,style,time=0,windows_size=1):
        price_dic, volume_dic, feedback_dic, quick_dic, cash_dic, interest_dict, stru1, stru2, stru3, risk_dic, store_dic=self.get_dic()

        if style=="pre":
            f_pre_result = open("D:/stock_data2.0/pre_result.csv", "w+")
            f_pre_data = open("D:/stock_data2.0/pre_data.csv", "w+")
        if style=="train":
            f_train_data = open("D:/stock_data2.0/train_data.csv", "w+")
        j=0
        if (style == "pre"):
            time += 1
        for key in price_dic:
            j+=1
            try:

                list = []
                for i in range(time, time + 15):
                    list.append(price_dic[key][i])
                    list.append(str(float(volume_dic[key][i])/10000000))
                    list.append(feedback_dic[key][i])
                list.append(quick_dic[key])
                list.append(cash_dic[key])
                list.append(interest_dict[key])
                list.append(stru1[key])
                list.append(stru2[key])
                list.append(stru3[key])
                list.append(risk_dic[key])
                list.append(store_dic[key])
                if float(price_dic[key][time + 15 + windows_size])-float(price_dic[key][time + 15 + windows_size-1]) > 0:
                    list.append(1)
                else:
                    list.append(-1)

                if style == "train":
                    for i in range(len(list)):
                        f_train_data.write(str(list[i])[0:4] + " ")
                    f_train_data.write("\n")
                if style == "pre":
                    for i in range(len(list)):
                        f_pre_data.write(str(list[i]) + " ")
                    f_pre_data.write("\n")
                    f_pre_result.write(str(list[len(list)-1])+"\n")



            except :

                pass
        if style=="pre":
            f_pre_result.close()
            f_pre_data.close()
        if style=="train":
            f_train_data.close()
    def kernerl(self,style,segement):
        f_train_data=open("D:/stock_data2.0/%s_data.csv"%style, "r")
        f_train_kernel=open("D:/stock_data2.0/%s_kernel.csv"%style, "w+")
        landmark=[]
        result_list=[]
        for line in f_train_data.readlines()[segement*100:segement*100+202]:
            mark=[]
            line=line.split()
            for feature in line:
                mark.append(float(feature))
            result_list.append( mark.pop(len(mark)-1))
            landmark.append(mark)

        i=0
        for x in landmark:
            # print(i)
            f=self.RBF(landmark, x)
            for data in f:
                if(data>10000000000): data=1000000000
                f_train_kernel.write(str(data)+",")
            f_train_kernel.write(str(result_list[i])+",")
            f_train_kernel.write("\n")
            i += 1
        f_train_kernel.close()
        f_train_data.close()

    def RBF(self,landmark,x):
            f=[]
            x=np.array(x)
            for l in landmark:
                l=np.mat(l)
                f.append(np.exp((np.sum(np.square(l-x)))/1000))
            return f
    def build_kernal(self,segement):
        self.kernerl("train",segement)
        self.kernerl("pre",segement)
    def build_day(self,time=0,window_size=1):
        self.build_data("train", time,window_size)
        self.build_data("pre",time, window_size)



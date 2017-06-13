import requests
class Data_getter:
    def get_data(self):
        self.__get_one_style_data("train")
        self.__get_one_style_data("test")
    def build_one_stock(self,stock_num):
        f_data = open("D:/stock_data/trian_data.csv" )
        f_output_data = open("D:/stock_data/%s_current_data.csv"%stock_num , "w+")
        f_output_result = open("D:/stock_data/%s_result.csv" % stock_num, "w+")
        for line in f_data:
            try:
                output, result, label = self.__build_one_line(line.split(), 0, "softmax")
            except:
                continue
            f_output_data.write(str(label)[2:] + ",")
            for i in range(len(output)):
                f_output_data.write(str(output[i]) + ",")

            f_output_data.write("\n")

            f_output_data.write(str(label)[2:] + ",")
            for i in range(len(output)):
                f_output_data.write(str(output[i]) + ",")
            f_output_data.write("\n")

            f_output_result.write(str(label)[2:] + "   " + str(result) + "\n")
        f_output_data.close()
        f_output_result.close()


    def __get_one_style_data(self,style):
        f_num = open("D:/stock_data/%s_number.txt"%style )
        f_data=open("D:/stock_data/%s_data.csv"%style,"w+")
        nums=f_num.read().split()
        for i in range(len(nums)):
            print("getting %s data in %dth line"%(style,i))
            try:
                r=requests.get("http://data.gtimg.cn/flashdata/hushen/weekly/%s.js"%(nums[i]))
            except:
                print("cannot get connected with the server,try next url")
                continue
            result=r.text.split()
            price = result[2:550:6]
            f_data.write(str(nums[i])+" ")
            for j in range(len(price)):
                f_data.write(str(price[j])+" ")
            f_data.write("\n")
        f_data.close()
    def build_test_data(self,num,model_style):
        self.__build_one_style("test", num.model_style)
    def build_data(self,num,model_style):
        self.__build_one_style("train",num,model_style)
        self.__build_one_style("test", num,model_style)
    def __build_one_style(self,style,num,model_style):
        f_data=open("D:/stock_data/%s_data.csv"%style )
        f_output_data=open("D:/stock_data/%s_current_data.csv"%style,"w+")
        f_output_result=open("D:/stock_data/%s_result.csv"%style,"w+")
        for line in f_data:
            try:
                output,result,label=self.__build_one_line(line.split(), num,model_style)
            except:
                continue
            f_output_data.write(str(label)[2:]+",")
            for i in range(len(output)):
                f_output_data.write(str(output[i])+",")

            f_output_data.write("\n")
            f_output_data.write(str(label)[2:] + ",")
            for i in range(len(output)):
                f_output_data.write(str(output[i]) + ",")
            f_output_data.write("\n")

            f_output_result.write(str(label)[2:]+"   "+str(result)+"\n")
        f_output_data.close()
        f_output_result.close()
    def __build_one_line(self,price,num,model_sytle):

        if(model_sytle=="softmax"):
            return self.__build_one_line_softmax(price,num)
        if(model_sytle=="svm"):
            return self._build_one_line_svm(price,num)
    def _build_one_line_svm(self,price,num):
        if (len(price) - num < 51):
            raise NameError
        delta = []
        for i in range(len(price) - num - 50, len(price) - num):
            delta.append(float(price[i]) - float(price[i - 1]))
        result=1 if delta[len(delta)-1]>0   else 0
        delta.pop(len(delta) - 1)
        delta.append(result)
        label = price[0]
        return delta,result, label
    def __build_one_line_softmax(self, price, num):
        if (len(price)-num < 51):
            raise NameError
        delta = []
        for i in range(len(price) - num - 50, len(price) - num):
            delta.append(float(price[i]) - float(price[i - 1]))
        example = []
        one_position = 100 + int(delta[len(delta) - 1] / float(price[len(price) - 1]) * 100)
        if (one_position < 0): raise NameError
        for i in range(200):
            if i == one_position:
                example.append(1)
                continue
            example.append(0)
        delta.pop(len(delta) - 1)
        inputs = delta + example
        label=price[0]
        return inputs,one_position,label






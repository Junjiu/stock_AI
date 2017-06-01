import  requests
class Pair:
  delta=0;
  p_delta=0


def compare(pair):
    return pair.p_delta
class Tester:

    def test(self,top=10):
        pairs,total=self.get_pairs()
        if top>len(pairs) : top=len(pairs)
        sum,num = 0,0

        for i in range(top):
            if pairs[i].p_delta<0:
                break
            # print ("pre:"+str(pairs[i].p_delta))
            # print("true:" + str(pairs[i].delta))
            sum += pairs[i].delta
            num += 100
            #
            # print("true:")
            # print(pairs[i].delta)
            # print("predict")
            # print(pairs[i].p_delta)
        print("Total in this week: %f"%total)
        print("Interest in this week: %f"%(sum/num))
        return total,(sum/num)
    def get_pairs(self):
        file1 = open("D:/stock_data/predict_result.csv")
        text1 = file1.read().split()
        file2 = open("D:/stock_data/test_result.csv")
        text2 = file2.read().split()
        pairs = []
        sum = 0
        total = 0
        i,j = 0,0
        while True:
            if(i>=len(text1) or j>=len(text2)):
                break
            while(text1[i]!=text2[j]):
                if(text1[i]>text2[j]):
                    j+=2
                else:
                    i+=2
            if (i >= len(text1) or j >= len(text2)):
                break
            if (float(text1[i]) < 100 or float(text2[j]) < 50):
                continue
            i+=1;
            j+=1;
            delta = float(text2[i]) - 100
            p_delta = float(text1[i]) - 100
            p = Pair()
            p.p_delta = p_delta
            p.delta = delta
            pairs.append(p)
            total += delta
            sum+=100
            i += 1;
            j += 1;
        print("number of stocks"+str(sum/100))
        file1.close()
        file2.close()
        pairs.sort(key=compare, reverse=True)
        return pairs,total/sum
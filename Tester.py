import  requests
class Pair:
  delta=0;
  p_delta=0


def compare(pair):
    return pair.p_delta
class Tester:

    def test(self,top=20):
        pairs,total=self.get_pairs()
        if top>len(pairs) : top=len(pairs)
        sum,num = 0,0

        for i in range(top):
            sum += pairs[i].delta
            num += 100
            # print("true:")
            # print(pairs[i].delta)
            # print("predict")
            # print(pairs[i].p_delta)
        print("Total: %f"%total)
        print("Prediction: %f"%(sum/num))
        return total,(sum/num)
    def get_pairs(self):
        file1 = open("D:/stock_data/predict_result.csv")
        text1 = file1.read().split()
        file2 = open("D:/stock_data/test_result.csv")
        text2 = file2.read().split()
        pairs = []
        sum = 0
        total = 0
        for i in range(min(len(text1), len(text2))):
            if (float(text1[i]) < 100 or float(text2[i]) < 80):
                continue
            delta = float(text2[i]) - 100
            p_delta = float(text1[i]) - 100
            p = Pair()
            p.p_delta = p_delta
            p.delta = delta
            pairs.append(p)
            total += delta
            sum+=100
        file1.close()
        file2.close()
        pairs.sort(key=compare, reverse=True)
        return pairs,total/sum
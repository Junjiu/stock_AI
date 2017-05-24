class Pair:
  delta=0;
  p_delta=0
def compare(pair):
  return pair.p_delta

file1=open("D:/stock_data/predict_result.csv")
text1=file1.read().split()
file2=open("D:/stock_data/test_result.csv")
text2=file2.read().split()
pairs=[]
sum=0
num=0
dic={}
total=0
print(text2[7])
for i in range(min(len(text1),len(text2))):
  if(float(text1[i])<100 or float(text2[i])<80):
    continue
  delta=float(text2[i])-100
  p_delta=float(text1[i])-100
  p=Pair()
  p.p_delta=p_delta
  p.delta=delta
  pairs.append(p)
  total+=delta

pairs.sort(key=compare,reverse=True)

for i in range(20):
  sum+=pairs[i].delta
  print("delta: %f,  p_delta: %f"%(pairs[i].delta,pairs[i].p_delta))
  num+=100
print(sum)
print(num)
print("interest")
print(sum/num*100)
print("total:")
print(total)

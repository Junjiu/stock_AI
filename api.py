import requests
f = open("D:/stock_data/test_data.csv", "w+")
f_re=open("D:/stock_data/test_result.csv", "w+")
def get_data(url):

    try:
        print(url)
        r = requests.get(url)
        result = r.text.split()
        price = result[2:525:6]
        if(len(price)<50) :
            price("Bad data")
            raise NameError
        delta = []
        print(len(price))
        for i in range(len(price)-50, len(price)):
            delta.append(float(price[i]) - float(price[i - 1]))
            print(price[i])
        example = []
        one_potion = 100 + int(delta[len(delta) - 1] / float(price[len(price) - 1]) * 100)
        if(one_potion<0) :raise  NameError
        print(one_potion)
        print("last  delta and value %s,  %s"%(delta[len(delta) - 1],float(price[len(price) - 1])))
        #print(one_potion)
        #print(delta[len(delta) - 1])
        #print(price[len(price) - 1])
        for i in range(199):
            if i == one_potion:
                example.append(1)
                continue
            example.append(0)
        delta.pop(len(delta) - 1)
        #print("delta's length: %s" % len(delta))
        #print("example's length :  %s" % len(example))
        inputs = delta + example
        #print(inputs)
        for i in range(len(inputs)):
            f.write(str(inputs[i]) + ",")
        f.write("\n")
        f_re.write(str(one_potion))

        f_re.write("\n")
        print("Success.")
    except:
        print("Error!")
        pass
file=open("D:/stock_data/test_number.txt")

nums=file.read().split()
for i in range(len(nums)):
    get_data("http://data.gtimg.cn/flashdata/hushen/weekly/%s.js"%(nums[i]))
    print("writing  %dth line's data"%i)
f.close()
f_re.close()
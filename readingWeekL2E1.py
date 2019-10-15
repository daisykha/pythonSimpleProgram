def minPrecipitation(ls):
    min=ls[0]
    for i in ls:
        if i<min:
            min = i
    return min

def maxPrecipitation(ls):
    max=ls[0]
    for i in ls:
        if i>max:
            max = i
    return max

def averagePrecipitation(ls):
    sum=0
    for i in ls:
        sum+=i
    return sum/len(ls)

with open('precipitations-world.txt', 'r') as textFile:
    data = textFile.read()  
my_list = data.splitlines()

pre = []
for i in my_list:
    for ch in i:
        if ch==",":
            pre.append(float(i[5:]))

print(minPrecipitation(pre))
print(maxPrecipitation(pre))
print(averagePrecipitation(pre))



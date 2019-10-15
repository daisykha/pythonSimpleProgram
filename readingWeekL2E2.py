with open("precipitations-world.txt","r") as text_file:
    data=text_file.read()
preWorld=data.splitlines()
lsW=[]
for i in preWorld:
    lsW.append(i[5:])

with open("precipitations-NAmerica.txt","r") as text_file:
    data=text_file.read()
preNA=data.splitlines()
lsNA=[]
for i in preNA:
    lsNA.append(i[5:])

with open("precipitations-Europe.txt","r") as text_file:
    data=text_file.read()
preEurope=data.splitlines()

newls=[]
newls = preEurope



for i in range(len(preWorld)):
    newls[i] += ("," + lsNA[i] + "," + lsW[i])


filename = open("test1.txt","w")
for i in newls:
    filename.write(i)
    filename.write("\n")
filename.close()

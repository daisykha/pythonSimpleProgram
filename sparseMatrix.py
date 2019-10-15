def dimension(matrix):
    row=[]
    column=[]
    for i in matrix:
        k = i.index(",")
        row.append(int(i[:k]))
        column.append(int(i[k+1:]))
    max1=0
    max2=0
    for i in row:
        if i>max1:
            max1=i
    for j in column:
        if j>max2:
            max2=j
    return max1,max2

def addTwoMatrices(matrix1,matrix2):
    add = {}
    for i in matrix1:
        for j in matrix2:
            if i == j:
                add[i] = matrix1[i]+matrix2[j]
    return add

def transpose(matrix):
    row=[]
    column=[]
    for i in matrix:
        k = i.index(",")
        row.append(int(i[:k]))
        column.append(int(i[k+1:]))

    t={}
    k1=""
    k2=""
    for i in range(len(matrix)):
        k1 = str(row[i]) + "," + str(column[i])
        k2 = str(column[i])+","+str(row[i])
        t[k2] = matrix.get(k1,None)
                 
    return t

    

dic1= {"1,3":3,"2,1":5,"4,3":6, "1,4":3}
dic2= {"1,3":5,"4,3":2,"3,2":4}
        
#print(dimension(dic1))
#print(addTwoMatrices(dic1,dic2))
print(transpose(dic2))


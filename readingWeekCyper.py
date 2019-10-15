def encode(cyper,number):
    temp=[]
    s=""
    for i in number:
        temp.append(i)
    for i in temp:
        s += cyper.get(int(i)) + " "
    return s

def decode(cyper,number):
    temp = []
    s=""
    j=0
    m=""
    for i in number:
        if j !=4:
            s+=i
            j+=1
        elif j == 4:
            temp.append(s)
    for i in temp:
        print(cyper[i])
    return m

        
decypherbook = {'0000':8, '0001':1, '0010':0, '0011':9,
                '0100':5, '0101':3, '0110':7, '0111':2,
                '1110':4, '1111':6}

cypherbook   = {8:'0000', 1:'0001', 0:'0010', 9:'0011',
                5:'0100', 3:'0101', 7:'0110', 2:'0111',
                4:'1110', 6:'1111'}

number = input("Enter number: ")
#print(encode(cypherbook,number))
print(decode(cypherbook,number))

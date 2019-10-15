def printBasePattern(n,p1,p2):
    s=""
    for i in range(n):
        for j in range(n):
            if i == j or i == n - j -1 :
                s=s+p1
            else:
                s=s+p2
        s=s+"\n"
    return s

def printMultipleBasePattern(r,c):
    for i in range(r):
        for j in range(c):
            print(printBasePattern(n,"o","_"),end="")
        print()
    
n = int(input("Enter n: "))
if n <3:
    raise ValueError("n must be more than or equal 3")
else:
    print(printMultipleBasePattern(2,3))



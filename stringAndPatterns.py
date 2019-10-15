def printBasePattern(n):
    for i in range(n):
        for j in range(n):
            if i == j or i == n - j -1 :
                print("X",end="")
            else:
                print(".",end="")
        print()

n = int(input("Enter n: "))
if n <3:
    raise ValueError("n must be more than or equal 3")
else:
    printBasePattern(n)

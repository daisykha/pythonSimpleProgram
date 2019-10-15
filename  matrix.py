def scalar_product(m,scalar):
    k=[[0 for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            k[i][j] = scalar * m[i][j]
    return k   

def transpose(m):
    at=[[0 for i in range(r)] for j in range(c)]
    for i in range(c):
        for j in range(r):
            at[i][j]=(m[j][i])
    return at
        
scalar = int(input("Enter a scalar: "))
c = int(input("Enter the number of columns in a matrix: "))
r = int(input("Enter the number of rows in a matrix: "))

a=[[0 for i in range(c)] for j in range(r)]

for i in range(r):
   for j in range(c):
        print("Enter m[",i,"][",j,"]: ")
        a[i][j] = int(input(""))

print(a)
print("\n")

print(scalar_product(a,scalar))
print(transpose(a))



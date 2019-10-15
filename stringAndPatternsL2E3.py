n = int(input("Enter n: "))
if n <3:
    raise ValueError("n must be more than or equal 3")
else:
    for m in range(2):
        for i in range(n):
            for k in range(3):
                for j in range(n):
                    if j == i or i == n-j-1:
                        print('o',end='')
                    else:
                        print('-',end='')
            print()

    

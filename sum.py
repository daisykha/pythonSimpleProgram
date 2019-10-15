def sumNumbers(line):
    sum = 0
    k = line.split(" ")
    for i in k:
        sum  += int(i)
    return sum
        

def sumFromFile(filename):
    sum = 0
    with open(filename,"r") as input_file:
        for line in input_file:
            sum += sumNumbers(line)
    return sum

filename=input("Enter a file name: ")
print(sumFromFile(filename))

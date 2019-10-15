import random

while True:
    ask = input("Would you like to roll a dice?(y/n) ")
    if (ask != "y") and (ask!="n"):
        print("Invalid input. Please enter again. (y/n)")
    elif ask == "n":
        print("Press enter to exit")
        break
    else:
        die = random.randint(1,6)
        print(die)
        continue
    
    


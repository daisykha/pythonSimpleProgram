def concatDico(dico1,dico2):
   # try: 
        temp = {}
        temp = dico1.copy()
        temp.update(dico2)
        return temp
    #except KeyError:
       # print("There are 2 same keys in 2 dictionaries. Please try again.")
        
dict1 = {}
dict2 = {}

while True:
    print("Would you like to enter a pair to a dictionary 1? (y/n)")
    answer= input("")
    if answer == "y":
        key = input("Please enter key: ")
        value = input ("Please enter value: ")
        dict1[key]=value
    elif answer == "n":
        break
    else:
        print("Invalid choice. Please try again.")
        continue

while True:
    print("Would you like to enter a pair to a dictionary 2? (y/n)")
    answer= input("")
    if answer == "y":
        key = input("Please enter key: ")
        value = input ("Please enter value: ")
        dict2[key]=value
    elif answer == "n":
        break
    else:
        print("Invalid choice. Please try again.")
        continue
    
print(concatDico(dict1,dict2))

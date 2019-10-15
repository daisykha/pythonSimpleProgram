def check_palindrome(s):
    for i in range((len(s)//2)):
        if s[i]==s[-i-1]:
            return True
    return False

s = input("Enter the string: ")
if check_palindrome(s) == True:
    print("It is a palindrome")
else: print("It is not a palindrome")

##sjhfgjs

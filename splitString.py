import string
    
def splitString(text):
    word = ""
    ls = []
    if (text[len(text)-1] not in string.punctuation):
        text += "."
        
    for i in text:
        if (i == chr(32)) or (i in string.punctuation):
            if word=="":
                continue
            else:
                ls.append(word)
                word = ""
        else:
            word += i
    return ls

#sampleText =  "As Python's creator, I'd ''like to say a few words about its origins"
sampleText=""
f = open("test.txt", "r")
sampleText = f.read()
print(splitString(sampleText))




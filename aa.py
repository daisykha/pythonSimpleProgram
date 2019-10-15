import string
def calculateFrequency(text):
    alphabet = []
    for i in range(ord("a"),ord("z")+1):
        alphabet.append(chr(i))

    frequency = []
    for i in range(26):
        frequency.append(0)

    for j in range(len(text)):
        for i in alphabet:
            if text[j].lower() == i:
                p = alphabet.index(i)
                frequency[p] += 1

    for i in range(26):
        print("Letter",alphabet[i],":",frequency[i])
    
def calculateNumberOfWords(text):
    word = ""
    c=0
    if (text[len(text)-1] not in string.punctuation):
        text += "."
    for i in text:
        if (i==chr(32)) or (i in string.punctuation):
            if word=="":
                continue
            else:
                ls.append(word)
                word=""
        else:
            word +=i
    c = len(ls)
    return c

def averageLenOfWords(text):
    c = 0
    for i in ls:
        for ch in i:
            c += 1
    return int(c/len(ls))

def lengthFrequency(text):
    lf=[]
    l = []
    for i in ls:
        if len(i) in l:
            p = l.index(len(i))
            lf[p] += 1
        else:
            l.append(len(i))
            lf.append(1)
    for i in range(len(l)):
        print("Words with",l[i],"characters:",lf[i])

f = open("test.txt", "r")
sampleText = f.read()
print("Frequency of letters of the text: ")
ls = []
calculateFrequency(sampleText)
print("Number of words in text: ",calculateNumberOfWords(sampleText))
print("Average length of words = ",averageLenOfWords(sampleText))
print("Frequency of word length: ")
lengthFrequency(sampleText)

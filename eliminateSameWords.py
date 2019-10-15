import string
sampleText = ("As Python's creator, I'd like to say a few words about its "+
              "origins, adding a bit of personal philosophy.\n"+
              "Over six years ago, in December 1989, I was looking for a "+
              "'hobby' programming project that would keep me occupied "+
              "during the week around Christmas. My office "+
              "(a government-run research lab in Amsterdam) would be closed, "+
              "but I had a home computer, and not much else on my hands. "+
              "I decided to write an interpreter for the new scripting "+
              "language I had been thinking about lately: a descendant of ABC "+
              "that would appeal to Unix/C hackers. I chose Python as a "+
              "working title for the project, being in a slightly irreverent "+
              "mood (and a big fan of Monty Python's Flying Circus).")


def getWordsStartingWith(text, letter):
    word=""
    ls = []
    getWords =[]
    for i in text:
        for ch in i:
            if (ch == chr(32)) or (ch in string.punctuation):
                ls.append(word)
                word=""
            else:
                word +=ch

    for i in ls:
        if (i == chr(32)) or (i in string.punctuation):
            ls.remove(i)

    if letter.isupper():
        for i in ls:
            if (i[0] == letter) or (i[0].upper()==letter):
                getWords.append(i)
    elif letter.islower():
        for i in ls:
            if (i[0] == letter) or (i[0].lower()==letter):
                getWords.append(i)
    return list(set(getWords))

letter = input("Please enter letter: ")
print(getWordsStartingWith(sampleText,letter))

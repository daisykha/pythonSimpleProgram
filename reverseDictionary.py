def reverseDictionary():
    for i in dico:
        t = i
        i = dico[t]
        dico[i] = t
    print(dico)
        
dico = {"one":1, "two":2}

reverseDictionary()

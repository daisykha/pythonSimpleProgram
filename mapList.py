def mapList(key, value):
    t={}
    try:
        for i in range(len(key)):
            t[key[i]] = value[i]
        return t
    except KeyError:
        print("There are 2 same keys. Please try again.")


ls1 = ["one","two","one"]
ls2 = [1,2,3]
print(mapList(ls1,ls2))

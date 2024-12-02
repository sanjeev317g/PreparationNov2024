def characterAndCount():
    strin = "aabbccdd"
    count = 1
    compressed = []

    for n in range(1, len(strin)):
        if(strin[n] == strin[n-1]):
            count +=1
        else:
            compressed.append(strin[n-1] + str(count))
            count = 1
        
    compressed.append(strin[-1]+str(count))

    print(compressed)



characterAndCount()
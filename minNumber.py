def minNumber():
    min = [100,50,20,30,40,90]
    temp = min[0]
    for m in min[1:]:
        if m < temp:
            temp = m
    print (temp)

minNumber()

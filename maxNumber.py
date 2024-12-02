def maxNumber():
    max=[1,2,3,4,50,100,99]
    temp=max[0]
    for m in max[1:]:
        if  m >temp:
            temp = m
    print(temp)

maxNumber()


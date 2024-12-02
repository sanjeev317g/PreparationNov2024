def secondMax():
    secondM = [1,2,3,4,5,6,7,9,10,90]
    max = secondM[0]
    secondMax = secondM[0]
    for mx in secondM[1:]:
        if mx > max:
            secondMax = max
            max = mx
    print(max)
    print(secondMax)

secondMax()



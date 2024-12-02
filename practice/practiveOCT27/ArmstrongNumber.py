def armstrongNumber():
    number = 153
    str1 = len(str(number))
    
    count = 1
    amstrong = 0
    while(number !=0):
        number1 = int(number % 10)
        for n in range(str1):
            count = number1 * count
        amstrong = count + amstrong
        count = 1
        number = int(number / 10)
    print(amstrong)



armstrongNumber()
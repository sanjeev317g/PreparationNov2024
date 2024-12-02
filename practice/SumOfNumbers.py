def sumOfNumbers():
    number = 1234567

    digit = 0

    total = 0

    while(number != 0):

        digit = int(number % 10)

        total = int(total + digit)

        number = int(number /10)
    
    print(total)

sumOfNumbers()







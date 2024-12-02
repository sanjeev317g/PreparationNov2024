def ArmstrongNumber():
    number = 1634

    original = number

    length = str(number)

    number1 = 0

    number2 = 0

    number3 = 0
    for n in range(len(length)):

        number1 = int(number % 10)

        number2 = int(pow(number1, len(str(original))))

        number3 = int(number2 + number3)

        number = int(number / 10)
    
    print(number3)

ArmstrongNumber()



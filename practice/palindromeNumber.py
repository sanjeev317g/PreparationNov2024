def palindromeNumber():

    number = 12321

    rev = 0

    r = 0
    while(number != 0):

        r = int(number % 10)

        rev = int(rev * 10 + r)

        number = int(number / 10)
    
    print(rev)

palindromeNumber()

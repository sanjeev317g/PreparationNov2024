

def reverseNumber():
    rev = 0
    r = 0
    number = 56789
    while(number !=  0):

        r = int(number % 10)
        rev = int(rev * 10 + r)
        number = int(number / 10)

    print(rev)

reverseNumber()

print ("Aatish Kumar")

def primeNumber(number):
    for n in range(2, number):
        
        if(number % n == 0):
            return False
        
    return True


print(primeNumber(7))

def rangePrime(number):
    for n in range(number):
        if(primeNumber(n)):
            print(n)

rangePrime(20)


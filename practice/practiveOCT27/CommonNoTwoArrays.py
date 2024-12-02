
def CommonNumbers():
    a = [1,3,5,7,9,0,10] 
    b = [10,30,50,60,3,1]
    for n in list(a):
        for n1 in list(b):
            if(n == n1):
                print(n1)

CommonNumbers()

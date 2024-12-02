def febanacciSerice():
    n1 = 0
    n2 = 1
    n3 = 0
    for n in range(15):
        n3 = n1 + n2
        print("Fibanacci Serice : " , n3)
        n1 = n2
        n2 = n3

febanacciSerice()
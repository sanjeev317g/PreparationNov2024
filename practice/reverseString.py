def reverseString():
    str = "Automation"
    
    char = list(str)

    str1 = ""

    c = len(char)-1
    for n in reversed(char):
        str1 = n
        # print(str1)

def reverseStr():
    str = "Ttesting"
    
    char = list(str)

    for n in range(len(char) - 1, -1, -1):
        print(char[n])

reverseStr()
    

reverseString()


class Anagramss:
    def __init__(self):
        print("This")

def Anagram():
    str1 = "Listen"
    str2 = "Silent"
    str3 = len(str1.lower())
    str4 = len(str2.lower())
    if(str3 == str4):
        print("Step one matches and strinags are anagram")
    
    str3 = sorted(str1)
    str4 = sorted(str2)
    print(str3, str4)

    if(str3 == str4):
        print("dsfd sdfdsf")
        



a = Anagramss()

def Anagrams():
    str1 = "listen"
    str2 = "silent"

    str11 = {}
    str22 = {}

    for n in str1:
        if n in str11:
            str11[n] += 1
        else:
            str11[n] = 1
    for n in str2:
        if n in str22:
            str22[n] += 1
        else:
            str22[n] = 1
    if(str11 == str22):
        print("String in anagram")
        
Anagrams()


    

    



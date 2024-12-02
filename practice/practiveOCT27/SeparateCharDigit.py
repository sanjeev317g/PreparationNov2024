def CharDigit():
    s_str = "Test123"
    # c_chr = list(s_str)
    # print(c_chr)
    # for n in range(len(s_str)):
    chars = "".join([char for char in s_str if char.isalpha()])
    digits = "".join([char for char in s_str if char.isdigit()])
    print(chars)
    print(digits)
        
        
CharDigit()
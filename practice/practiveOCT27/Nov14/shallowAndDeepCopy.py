import copy

def C_Copy():
    original = [[1,2],[2,3]]
    c = copy.copy(original)
    d = copy.deepcopy(original)
    print(c)
    print(d)

C_Copy()
# List [], mutable, duplicates are allowed, will print the insertation order.
# Tuple (),im-mutable, prints the insrtation order
# Dictionary {"":""}, key value, one null key is allowed, keys cannot be duplicate, values can be duplicate, mutable

def dT_list():
    a = [1,2,3,"test"]
    # print(a.pop(0))
    # print(a)
    # a.insert(0,"car")
    # print(a)
    a.append("car1")
    # a.remove(3)
    # print(a)
    # a.sort()
    # print(a)
    # a.reverse()
    # print(a)
    # a.clear()
    b = ["New List", "New List1",1]
    a.extend(b)
    c = a.copy()
    c_count = c.count(1)
    i_index = c.index(1)
    c.insert(0,0)
    # c.pop(1)
    # c.remove(1)
    c.reverse()
    # c.sort()
    # print(c)
    # print(i_index)
    # print(c_count)

dT_list()

def tupil():
    t_tuple = (1,1.0,'a',"Test",1)
    # print(t_tuple)
    t_list = list(t_tuple)
    t_list.append("Mahes")
    t_list.insert(0,"swamy")

    # print(t_list)
    tt_tupe = tuple(t_list)
    # print(tt_tupe.count(1)) # this will return the number of the values present in the tuple.
    # print(tt_tupe.index('a')) # pass the value and this will return the index of the value.
    # print(tt_tupe,type(tt_tupe))


tupil()

def dictionary():
    d_dictionaty = {1:"Test1",2:"Test2",3:"Test3"}
    # d_dictionaty.clear()
    d_dic = d_dictionaty.copy()
    keys = ['age','country','work']
    # d_dic.fromkeys(keys,"Not availabe")
    # print(d_dic.fromkeys(keys,"Not availabe"))
    # print(d_dic.get(3,2))
    # print(d_dic.items())
    # print(d_dic.keys())
    #d_dic.pop(3)
    # print(d_dic.popitem())
    # print(d_dic.setdefault(2,''))
    d_dic.update()
    

    # print(d_dic)
dictionary()
    
def s_set():
    s_set = {1,1.1,'a',"Test"}
    


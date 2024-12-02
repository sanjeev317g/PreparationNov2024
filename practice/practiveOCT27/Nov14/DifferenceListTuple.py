class DifferenceListTuple:
    def oopsList(self):
        l_list = [1,2,0.1,'L']
        print("List is mutable")
        print("Defined with square Brackets")
        l_list.append('A')

        print(l_list)
    
    def oopsTuple(self):
        t_tuple = (1,2,0.1,'T')
        print("Tuple is immutable")
        print("Defined with paranthesis")
        print(t_tuple)

d = DifferenceListTuple()
d.oopsList()
d.oopsTuple()

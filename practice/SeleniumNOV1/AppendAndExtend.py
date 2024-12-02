class AppendExtend:
    def Append(self):
        l_list = [1,3,5]
        l_list.append(2)
        print(l_list)
    
    def Extend(self):
        l_list = [1,3,5]
        ll_list = [2,4,6]
        l_list.extend(ll_list)
        print(l_list)
    
ae = AppendExtend()
ae.Append()
ae.Extend()
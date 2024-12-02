class A:
    def aa(self):
        print("from A class")

class B:
    def bb(self):
        print("from B class")
    
class C(A,B):
    def cc(self):
        print("from C class")

c = C()
c.aa()
c.bb()
c.cc()



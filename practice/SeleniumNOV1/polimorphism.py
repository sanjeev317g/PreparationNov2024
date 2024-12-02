class Animal:
    def eat(self,i,j):
        print("parent eat method")
        k = i+j
        return k
    
    def eat(self,a,b):
        print("second eat")
        c = a+b
        return c

class Cat(Animal):
    def eat(self,a,b):
        print("Cat child eat method")
        c = a+b
        return c

class Dog(Animal):
    def eat():
        print("Dog child eat method")

a = Cat()
# a.eat("bat","mat")
a.eat(10,20)

